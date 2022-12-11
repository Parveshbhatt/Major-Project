from flask import render_template, redirect, session
def home(records):
    login = False
    if "email" in session:
        email = session["email"]
        record = records.find_one({"email": email})
        predictSheetLink = record['predictSheetLink']

        login = True
        return render_template('home.html',login = login, predictSheetLink= predictSheetLink) 
    return render_template('home.html',login = login) 

