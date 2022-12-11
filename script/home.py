from flask import render_template, redirect, session
def home(records):
    login = False
    email = session["email"]
    if "email" in session:
        record = records.find_one({"email": email})
        predictSheetLink = record['predictSheetLink']

        login = True
        print(login)
    return render_template('home.html',login = login, predictSheetLink= predictSheetLink) 

