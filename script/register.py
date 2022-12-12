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
        sheetName = "rpi-temp"
        predictSheetName = "dataFromPi"
        predictSheetLink = "https://docs.google.com/spreadsheets/d/1Xov2lmL8Z35Ud5p4ieednIokc4F52uS6MPTae77yso8/edit?usp=sharing" 
        sheetLink = "https://docs.google.com/spreadsheets/d/1ZP_pBORadOK5wF0GjkaQgKyuHDL70hW_d_GKFaNhk7k/edit?usp=sharing" 
        
        user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})
        ip_found = records.find_one({"ipAddress": ipAddress})
        if user_found:
            message = 'There already is a user by that name'
            return render_template('register.html', message=message)
        if email_found:
            message = 'This email already exists in database'
            return render_template('register.html', message=message)
        if password1 != password2:
            message = 'Passwords should match!'
            return render_template('register.html', message=message)
        if ip_found:
            message = 'This Ip address exists in database'
            return render_template('register.html', message=message)
        else:
            # hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            # user_input = {'name': user, 'email': email, 'password': hashed}
            user_input = {'username': user, 
                'email': email, 
                'password1': password1, 
                'password2': password2, 
                'ipAddress' : ipAddress, 
                'match' : match,
                'sheetName' : sheetName,
                'predictSheetName' : predictSheetName,
                'sheetLink' : sheetLink,
                'predictSheetLink' : predictSheetLink

            }
            records.insert_one(user_input)
            return redirect('/login')
    return render_template('register.html')