# Major-Project

### Environmental Condition Monitoring System based on Edge-Fog Computing using Machine Learning


### Master Node
A master node is a fog node that is responsible for coordinating the activities of the worker nodes. It is responsible for distributing tasks to the worker nodes, collecting the results from the worker nodes, and aggregating the results. A worker node can login on the master node and can access the predictions and in the situation of load on worker node, the master node come into action. First of all it checks the worker authentication, if the worker is valid it reads the latest reading from the google sheet of that specific worker node and perform necessary computation with ML model to generate the prediction and displays it on predict page. On the other hand, if the worker is not valid then it render to the Wrong Worker Page.
### Setup of Master Node
Steps followed for setting up master node:
1. Git clone the master branch.
2. Install the libraries using command : 

		pip install flask numpy pandas pickle scikit-learn pymongo

3. Download Google Auth.json file from [Google-auth.json](https://drive.google.com/file/d/1HkV1gi5XPWU2rzTopRKkmC2RtRE8gvyL/view?usp=sharing "Google-auth.json") and place this file in the scripts folder. This file will allow you to read and write into google sheets using Google Sheets API.



### Folder Structure

The master node consists of following files and folders : 

**csv/ :** Consists csv files for ML model training. Book2.csv was used to train the model.

**ml code/ :**
Consists code for ML model in both .ipynb and .py file

**script/ :** 
Consists of all the functions for the application created in the form of different files
- Error404.py:  Python file which handles the functionality of 404 (Page Not Found) Page.
- home.py: Python file which handles the functionality of home page
- login.py: Python file which handles the functionality of login page
- predict.py: Python file which handles the functionality of predict page
- readGoogleSheet.py: Python file which handles the functionality of reading google sheets
- register.py: Python file which handles the functionality of register page
- writeToGs.py: Python file which handles the functionality of writing to google sheets.

**static/css/ :** 
Contains styles.css which handles the styling of web pages

**templates/:** 
Contains templates for different pages of the application

- 404.html: html page template for 404 page
- home.html: html page template for home page
- login.html: html page template for login page
- register.html: html page template for register page
- predict.html: html page template for predict page
- wrongWorker.html: html page template for wrong worker page
- base.html : html template consisting of pieces of code which are common to all the above pages

**app.py:**  Entry point to the whole application. Flask will run this file for the running the whole application



###  How to use the Application

Run the following command in terminal to run the application: 

	python app.py
		
Follow the link displayed on the terminal:
http://127.0.0.1:5000/

Email: worker1@gmail.com

Password: worker1

After logging in successfully you can view the current temperature and humidity with the prediction Rain Today.
You can view the past predictions by clicking on the History button on the navbar.
