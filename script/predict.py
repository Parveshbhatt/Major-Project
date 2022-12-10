import pickle
from script.csvImport import *
from script.csvAppend import *
from script.readGoogleSheet import * 
from script.load import *
from script.writeToGs import *  
from script.ip import *
from flask import render_template, redirect, session

#for Adafruit data
from Adafruit_Python_DHT.examples.google_spreadsheet import *

def predict(records):
    if  "email" in session:
        email = session["email"]
        record = records.find_one({"email": email})
        match = record['match']
        ip1 = record['ipAddress']
        ip2 = getIp()
        if(match):
            if(loadCheck() == True):
                return render_template("loadOnWorker.html")
            # load the model
            model = pickle.load(open('./models/svm.pkl', 'rb'))
            
            # import required csv 
            #localCSVInput = import_csv("DhtDatalogger\dhtReading.csv")
            #googleCSVInput = read_csv('rpi-temp')
            # extract the input from the csvs
            #googleInput = googleCSVInput[0]
            #localInput = localCSVInput[-1]
            localInput = getData()
            while(localInput == []):
                time.sleep(2)
                localInput = getData()
            # import the output csv
            outputCSV = import_csv("results.csv")
            outputLastRow = []
            if(len(outputCSV) != 0):
                outputLastRow = outputCSV[-1]
            # input to be given to model
            inputArray = localInput
            tempHumInput = [[inputArray[3],inputArray[2]]]
            # getting the prediction from model
            prediction = model.predict(tempHumInput)
            # appending the required string according to prediction
            rain = "No"
            if(prediction[0] == 1):
                rain = "Yes"
            while(True):
                if(inputArray[-1] != "Yes" and inputArray[-1] != "No"):
                    inputArray.append(rain)
                    break

            # appending output array to the results.csv
            outputArray = inputArray
            if(len(outputCSV) == 0 or  
            (outputArray[2] != outputLastRow[2] and 
            outputArray[3] != outputLastRow[3]and 
            outputArray[4] != outputLastRow[4])):
                writeToCsv(outputArray)
                WriteToGs(outputArray)

            return render_template('predict.html',
            prediction_text='Rain Today: {}'.format(outputArray[-1]),
            temperature=' {}'.format(outputArray[-3]),
            humidity=' {}'.format(outputArray[-2])) 
        elif(ip1 == ip2):
            match = True
            records.update_one( { "email": email}, { "$set": { "match": True } })
            return redirect("/predict")
        else:
            return render_template("wrongWorker.html")
    return redirect("/login")

