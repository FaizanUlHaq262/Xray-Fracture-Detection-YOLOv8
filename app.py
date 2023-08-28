from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import cv2
import numpy as np
from ultralytics import YOLO

app = Flask(__name__)

# Load your YOLO model here (replace this with actual model loading)
model = YOLO(r'model\best.pt')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #create directory for storing uploaded images and predictions
        if not os.path.exists('static'):
            os.mkdir('static')
        if not os.path.exists('static/uploads'):
            os.mkdir('static/uploads')
        if not os.path.exists('static/predictions'):
            os.mkdir('static/predictions')
            
        # Get uploaded image from the form
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            image_path = os.path.join(r'static\uploads', uploaded_file.filename)
            uploaded_file.save(image_path)

            # Load and process the image
            image = cv2.imread(image_path)  # Load the image
            # Process the image
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (640, 640))
            # Run the YOLO model to make predictions
            predictions = model.predict(image)  # Replace with your actual prediction code
            
            #count of fractures
            counter = 0
            counter = len(predictions[0].boxes.data) #get the count of fractures
            # Process predictions and display predictions
            predIMG=0
            for result in predictions:                                         # iterate predictions
                boxes = result.boxes.cpu().numpy()                         # get boxes on cpu in numpy
                for box in boxes:                                          # iterate boxes
                    r = box.xyxy[0].astype(int)                            # get corner points as int
                    print(r)                                               # print boxes
                    predIMG = cv2.rectangle(predictions[0].orig_img, r[:2], r[2:], (255, 255, 255), 2)   # draw boxes on img

            # Save the image with bounding boxes
            predFileName = f'{uploaded_file.filename[:uploaded_file.filename.find(".")]}_predictions.{uploaded_file.filename[uploaded_file.filename.find(".")+1:]}'
            predFilePath = os.path.join(r'static\predictions', predFileName)
            cv2.imwrite(predFilePath, predIMG)
            
            return render_template('index.html', predictions=predFilePath, image_path=image_path , counter=counter)
    return render_template('index.html')

@app.route('/download/<filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
