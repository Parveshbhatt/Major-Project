from flask import render_template, redirect, session
def home():
    login = False
    if "email" in session:
        login = True
        print(login)
        return render_template('home.html',login = login) 

