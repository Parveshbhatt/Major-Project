from flask import Flask, render_template, request, url_for, redirect, session
# import bcrypt
def login(records):
    message = 'Please login to your account'
    if "email" in session:
        return redirect('/predict')

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        email_found = records.find_one({"email": email})
        if email_found:
            email_val = email_found['email']
            passwordcheck = email_found['password1']
            # if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
            if password == passwordcheck:
                session["email"] = email_val
                return redirect('/predict')
            else:
                if "email" in session:
                    return redirect('/login')
                message = 'Wrong password'
                return render_template('login.html', message=message)
        else:
            message = 'Email not found'
            return render_template('login.html', message=message)
    return render_template('login.html', message=message)