from __future__ import division, print_function

import sys
import os
import glob
import re
import numpy as np


from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename


app = Flask(__name__)

MODEL_PATH ='vgg16.h5'


model = load_model(MODEL_PATH)




def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    img = np.asarray(img)
    img = np.expand_dims(img, axis=0)
    output = model.predict(img)
    if output[0][0] == 1.0:
        output = 'Buildings'
    elif output[0][1] == 1.0:
        output = 'Forest'
    elif output[0][2] == 1.0:
        output = 'Glacier'
    elif output[0][3] == 1.0:
        output = 'Mountain'
    elif output[0][4] == 1.0:
        output = 'Sea'
    else:
        output = 'Street'
    
    return output


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        prediction = model_predict(file_path, model)
        result=prediction
        return result
    return None	


if __name__ == '__main__':
    app.run(debug=True)
