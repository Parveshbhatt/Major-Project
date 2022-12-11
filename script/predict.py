import pickle
from script.readGoogleSheet import * 
from script.writeToGs import *  
from flask import render_template, redirect, session
def predict(records):
    if  "email" in session:
        email = session["email"]
        record = records.find_one({"email": email})
        match = record['match']
        sheetName = record['sheetName']
        predictSheetName = record['predictSheetName']
        predictSheetLink = record['predictSheetLink']

        if(match):
            # load the model
            model = pickle.load(open('./models/svm.pkl', 'rb'))
            # import required csv 
            googleCSVInput = read_csv(sheetName)
            # extract the input from the csvs
            googleInput = googleCSVInput[0]
            # import the output csv
            outputCSV = read_csv(predictSheetName)
            outputLastRow = []
            if(len(outputCSV) != 0):
                outputLastRow = outputCSV[0]
                print(outputLastRow)
            # input to be given to model
            inputArray = googleInput
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
                WriteToGs(predictSheetName,outputArray)

            return render_template('predict.html',
            predictSheetLink= predictSheetLink,
            prediction_text='Rain Today: {}'.format(outputArray[-1]),
            temperature=' {}'.format(outputArray[-3]),
            humidity=' {}'.format(outputArray[-2])) 
        else:
            return render_template("wrongWorker.html")
    return redirect("/login")

