import pickle
from script.csvImport import *
from script.csvAppend import *
from script.readGoogleSheet import * 
from flask import render_template, redirect, session
from datetime import datetime
def predict():
    if "email" in session:
        email = session["email"]
        # for worker
        data = import_csv("DhtDatalogger\dhtReading.csv")
        # for master
        data = read_csv()
        output = import_csv("results.csv")
        # for worker
        # predictionData= data[-1]
        # for master
        predictionData = data[0]
        outputData = []

        if(len(output) != 0):
            outputData = output[-1]

        appendToCsv = output[-1]
        last_row = [[predictionData[3], predictionData[2]]]

        model = pickle.load(open('./models/svm.pkl', 'rb'))

        today = datetime.now()
        date = today.strftime("%d/%m/%Y %H:%M:%S")
        date = date.split(" ")
        
        prediction = model.predict(last_row) 
        rain = "No"
        if(prediction[0] == 1):
            rain = "Yes"
        while(True):
            if(appendToCsv[-1] == "Yes" or appendToCsv[-1] == "No"):
                break                
            else:
                appendToCsv.insert(2, rain)
                break
        appendToCsv.insert(0, date[0])
        appendToCsv.insert(1, date[1])
        if(len(outputData) == 0):
            writeToCsv(appendToCsv)
        else:
            if(appendToCsv[2] != outputData[1] and appendToCsv[3] != outputData[0]):
                writeToCsv(appendToCsv)
        return render_template('predict.html',
        prediction_text='Rain Today: {}'.format(rain),
        temperature=' {}'.format(predictionData[2]),
        humidity=' {}'.format(predictionData[3])) 
    return redirect("/login")
