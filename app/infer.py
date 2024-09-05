import torch
import cv2
import numpy as np
import torchvision.transforms as transforms
import torchvision.models as models
import torch.nn as nn
import torch.nn.functional as F

# Define the Model class if not already defined
class Model(nn.Module):
    def __init__(self, num_classes, latent_dim=2048, lstm_layers=1, hidden_dim=2048, bidirectional=False):
        super(Model, self).__init__()
        model = models.resnext50_32x4d(weights='DEFAULT')
        self.model = nn.Sequential(*list(model.children())[:-2])
        self.lstm = nn.LSTM(latent_dim, hidden_dim, lstm_layers, bidirectional)
        self.relu = nn.LeakyReLU()
        self.dp = nn.Dropout(0.4)
        self.linear1 = nn.Linear(2048, num_classes)
        self.avgpool = nn.AdaptiveAvgPool2d(1)

    def forward(self, x):
        batch_size, seq_length, c, h, w = x.shape
        x = x.view(batch_size * seq_length, c, h, w)
        fmap = self.model(x)
        x = self.avgpool(fmap)
        x = x.view(batch_size, seq_length, 2048)
        x_lstm, _ = self.lstm(x, None)
        return fmap, self.dp(self.linear1(torch.mean(x_lstm, dim=1)))

def load_model(model_path):
    model = Model(num_classes=2).cuda()
    state_dict = torch.load(model_path)
    model.load_state_dict(state_dict, strict=False)
    model.eval()
    return model

def preprocess_frame(frame):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((224, 224)),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    frame = transform(frame)
    return frame

def process_video(video_path, model, seq_length=40):
    cap = cv2.VideoCapture(video_path)
    frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = preprocess_frame(frame)
        frames.append(frame)
        if len(frames) == seq_length:
            break

    cap.release()

    if len(frames) < seq_length:
        padding = [torch.zeros_like(frames[0]) for _ in range(seq_length - len(frames))]
        frames.extend(padding)

    frames = torch.stack(frames).unsqueeze(0).cuda()  # Shape: (1, seq_length, 3, 224, 224)

    with torch.no_grad():
        _, logits = model(frames)
        probabilities = F.softmax(logits, dim=1)
        _, prediction = torch.max(probabilities, 1)
        return prediction.item() == 0  # Assuming class 1 is "REAL"


def pipeline(video_path,model_path):
    model = load_model(model_path)
    res = process_video(video_path, model)

    if res:
        print("Prediction: REAL")
    else:
        print("Prediction: FAKE")
    return res

'''
# Main script
model_path = 'best.pt'

video_path_fake = 'arnold.mp4'# deepfake elon sample
video_path_real = 'thisiselon.mp4'# real elon sample


model = load_model(model_path)
is_real = process_video(video_path_fake, model)

if is_real:
    print("Prediction: REAL")
else:
    print("Prediction: FAKE")
'''