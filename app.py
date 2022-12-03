import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open('myPickle.pkl','rb'))


@app.route('/')
def home():
    #return 'Hello World'
    return render_template('home.html')
    #return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    inputs = list(request.form.values())
    weekday = int(inputs[0])
    month = int(inputs[1])
    holiday = bool(int(inputs[2]))
    hour = inputs[3]
    weather_main = inputs[4]
    clouds_all = inputs[5]
    temp = float(inputs[6])

    cols = ['holiday','temp','clouds_all','weather_main','weekday','hour','month']

    x = [holiday, temp, clouds_all, weather_main, weekday, hour, month]
    test_row = pd.DataFrame(x).transpose()
    test_row.columns = cols

    prediction = model.predict(test_row)
    print(prediction[0])

    #output = round(prediction[0], 2)
    return render_template('home.html', prediction_text="Traffic Flow Volume {}".format(prediction[0]))

if __name__ == '__main__':
    app.run(debug=True)