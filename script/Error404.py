from flask import render_template, redirect, session
def errorPage(records):
    login = False
    if "email" in session:
        email = session["email"]
        record = records.find_one({"email": email})
        username = record['username']
        predictSheetLink = record['predictSheetLink']

        login = True
        return render_template('404.html',login = login, predictSheetLink= predictSheetLink,
        username = username) 
    return render_template('404.html',login = login) 



