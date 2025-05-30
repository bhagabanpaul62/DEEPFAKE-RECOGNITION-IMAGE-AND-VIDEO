🕵️‍♂️ DEEPFAKE RECOGNITION
📖 Overview
DEEPFAKE RECOGNITION is a web application designed to identify deepfake videos and images using LSTM (Long Short-Term Memory) and ResNet (Residual Networks). This project aims to offer an accurate and reliable method for detecting manipulated media in both image and video formats. 🎥🔍

🚀 Features

- Deepfake Detection: Advanced LSTM and ResNet models for both video and image analysis 🤖
- High Accuracy: Effective in distinguishing between real and synthetic content ✅
- User-Friendly Web Interface: Easy-to-use interface for media processing and result display 🌟
- Real-Time Analysis: Quick processing and immediate results display 🚄
- Support for Multiple Formats: Handles both images and videos 📸

📥 Installation

1. Clone the repository:

```powershell
git clone https://github.com/bhagabanpaul62/DEEPFAKE-RECOGNITION-IMAGE-AND-VIDEO.git
cd DEEPFAKE-RECOGNITION-IMAGE-AND-VIDEO
```

2. Set up a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Make sure you have the pre-trained model:

- Place the `best.pt` model file in the `model/` directory
- Download link for the model will be provided upon request

🛠️ Usage

1. Start the Flask application:

```powershell
python main.py
```

2. Open your web browser and navigate to:

```
http://localhost:5000
```

3. Use the web interface to:

- Upload your video or image file
- Click 'Submit' to process
- View results showing if the content is REAL or GENERATED
- See the confidence score of the prediction

⚙️ Technical Stack

- Backend: Flask, PyTorch
- Deep Learning: LSTM, ResNet
- Image/Video Processing: OpenCV, PIL
- Frontend: HTML, CSS, JavaScript

🤝 Contributing
To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Commit your changes: `git commit -am 'Add new feature'`
5. Push to the branch: `git push origin feature/your-feature`
6. Create a pull request

📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

📬 Contact
For questions or feedback, email bhagabanpaulofficial@gmail.com 📧

🙏 Acknowledgements

- Libraries: Thanks to PyTorch, OpenCV, and Flask used in this project 🙌
- Datasets: Sourced from Kaggle Deepfake Detection Challenge 📚
- Contributors: Special thanks to all team members who contributed to this project 👥
