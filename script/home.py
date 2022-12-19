from flask import render_template, redirect, session
def home(records):
    print("Running Master Node:")
    login = False
    if "email" in session:
        email = session["email"]
        record = records.find_one({"email": email})
        username = record['username']
        predictSheetLink = record['predictSheetLink']
        match = record['match']
        login = True
        return render_template('home.html',login = login, predictSheetLink= predictSheetLink,
        username = username, match = match) 
    return render_template('home.html',login = login) 

