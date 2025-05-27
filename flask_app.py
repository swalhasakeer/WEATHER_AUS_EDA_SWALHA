from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
app = Flask(__name__)

with open('Rain Prediction(RFC) model.pkl','rb') as file:
  model = pickle.load(file)
  
with open('Scaler.pkl','rb') as file:
    scaler = pickle.load(file)

num_cols_std=['Location', 'Rainfall', 'WindGustDir', 'RainToday', 'Day', 'Month',
      'WindSpeed', 'Humidity', 'Pressure', 'Temperature']

@app.route('/')
def home():
  return render_template('index.html',prediction ="")

@app.route('/Predict', methods = ['POST'])
def index():
  
  input_data = {
    'Location':request.form['Location'],
    'Rainfall':float(request.form['Rainfall']),
    'WindGustDir':request.form['WindGustDir'],
    'RainToday':request.form['RainToday'],
    'Day':int(request.form['Day']),
    'Month':int(request.form['Month']),
    'WindSpeed':float(request.form['WindSpeed']),
    'Humidity':float(request.form['Humidity']),
    'Pressure':float(request.form['Pressure']),
    'Temperature':float(request.form['Temperature'])
  }
  input_df = pd.DataFrame([input_data])
  
  input_df['Location'] = LabelEncoder().fit_transform(input_df['Location'])
  input_df['WindGustDir'] = LabelEncoder().fit_transform(input_df['WindGustDir'])
  input_df['RainToday']=input_df['RainToday'].map({'No':0,'Yes':1})
  input_df[num_cols_std] = scaler.transform(input_df[num_cols_std])
  
  rain_prediction = model.predict(input_df)
  if rain_prediction == 0:
    predict = "It won't rain tomorrow"
  else:
    predict = "It will rain tomorrow"
  return render_template('index.html', prediction=predict)


if __name__ == '__main__':
    app.run(debug=True)