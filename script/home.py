import pickle
from script.csvImport import *

data = import_csv("Book2.csv")
temp = data[-1]
last_row = [[temp[1], temp[0]]]
model = pickle.load(open('./models/svm.pkl', 'rb'))
from flask import render_template, redirect, session
def home():
    if 'loggedin' in session:
        prediction = model.predict(last_row) 
        print(prediction)
        rain = "No"
        if(prediction[0] == 1):
            rain = "Yes"
        return render_template('index.html',
        username=session['username'],
        prediction_text='Rain: {}'.format(rain),
        temperature='Temperature: {}'.format(temp[0]),
        humidity='Humidity:{}'.format(temp[1])) 
    return redirect('/login/')
