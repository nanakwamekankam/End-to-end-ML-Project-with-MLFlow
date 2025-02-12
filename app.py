from flask import Flask, render_template, request
import os
import pandas as pd
import numpy as np
from mlProject.pipeline.prediction import PredictionPipeline


# Initialize Flask
app = Flask(__name__)

@app.route('/', methods=["GET"]) # Route to render homepage
def homepage():
    return render_template("index.html")

@app.route('/train', methods=["GET"]) # Route to training model 
def train():
    os.system('python3 main.py') # executes python3 main.py in terminal which runs through the pipeline
    return 'Training Successful'

@app.route('/predict', methods=['POST','GET']) # executes inference based on inputs and shows preductions
def predict():
    if request.method == 'POST':
        try:
            # reading the inputs given by the user
            fixed_acidity =float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
         
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1, 11)
            
            obj = PredictionPipeline()
            prediction = obj.predict(data)

            return render_template('results.html', prediction=str(prediction))

        except Exception as e:
            print('The Exception message is: ',e)
            return "Oops couldn't make prediction.\nCheck Inputs and try again.\nIf problem persists email nkankam@mail.bradley.edu with screenshots and a detailed explantion of the problem you encounter"
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
