from flask import Flask, render_template, request, url_for, redirect, session
# import bcrypt
from script.predict import *
def register(records):
    message = ''
    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")
        
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        ipAddress = request.form.get("ipAddress")
        match = False
        sheetCreated = False
        predictionSheetCreate = False
        sheetName = user
        predictSheetName = user + "Predict"
        predictionSheetName = predictSheetName 
        user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})
        if user_found:
            message = 'There already is a user by that name'
            return render_template('register.html', message=message)
        if email_found:
            message = 'This email already exists in database'
            return render_template('register.html', message=message)
        if password1 != password2:
            message = 'Passwords should match!'
            return render_template('register.html', message=message)
        else:
            # hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            # user_input = {'name': user, 'email': email, 'password': hashed}
            user_input = {'name': user, 
                'email': email, 
                'password': password2, 
                'ipAddress' : ipAddress, 
                'match' : match,
                'sheetCreated' : sheetCreated,
                'predictionSheetCreate' : predictionSheetCreate,
                'sheetName' : sheetName,
                'predictionSheetName' : predictionSheetName 
            }
            records.insert_one(user_input)
            return redirect('/login')
    return render_template('register.html')