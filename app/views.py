from flask import render_template,request
import os
import cv2
from app.infer import pipeline

UPLOAD_FOLDER ='static/upload'

def index():
    msg="UPLOAD THE IMAGE"
    if request.method == 'POST':
        f = request.files['file_name']
        filename = f.filename
        #save 
        path = os.path.join(UPLOAD_FOLDER,filename)
        f.save(path)
        # GET PRED
        model_path="model/best.pt"
        
        res=pipeline(path,model_path);
        if res:
         msg="REAL IMAGE"
        else:
         msg='GENERATED IMAGE'
    return render_template('index.html',message=msg)



'''
def app():
    return render_template('app.html')

def genderapp():
    return render_template('gender.html')'''