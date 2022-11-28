from flask import Flask
from flask_mysqldb import MySQL
from script.home import *
from script.login import *
from script.register import *


app = Flask(__name__) 
app.secret_key = 'jbibuibubaskcnakvccwefre'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Lokesh@423'
app.config['MYSQL_DB'] = 'pythonlogin'

# Intialize MySQL
mysql = MySQL(app) 

@app.route('/')
def h():
    return home()

@app.route('/login/', methods=['GET', 'POST'])
def l():
    return login(mysql)

@app.route('/register', methods=['GET', 'POST'])
def r():
    return register(mysql)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

# @app.route('/logout')
# def logout():
#     session.pop('username',None)
#     return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True)
