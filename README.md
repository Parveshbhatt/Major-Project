# Major-Project

### Environmental Condition Monitoring System based on Edge-Fog Computing using Machine Learning



### Worker Node
The worker node is responsible for measuring real-time data from the surroundings in the form of temperature and humidity and making the predictions corresponding to the real-time data. We have to maintain integrity between the master and worker so a login authentication system was used so that worker will work corresponding to its login credentials. To make the application secure the IP address of the worker was used. First registration is done with addition of IP of worker. After it checked whether the user has a valid worker or not by accessing the match variable from database (default value is false). Match variable makes sure that the IP address is matched only once and also helps to make sure at master node has valid user. At first, the IP address of the worker will be matched with the IP address entered during registration, if and only if both are the same then access the application and the match variable is updated to true in the database otherwise the user will be marked as invalid worker and not getting access the application. After the authentication of the worker the worker node reads the current temperature and humidity from the environment and sends to the ML model for predictions. Simultaneously it append the readings onto the corresponding Google Sheets. If any time worker fails then the user can access the application on the master.


### Setup of Worker Node :
Steps followed for setting up the worker node:
1. Connections of sensor with raspberry pi:

	The DHT22 sensor has three pins: VCC, DATA, and GND. To connect the DHT22 sensor to a Raspberry Pi, you will need to use jumper wires to connect the following pins:
		
	- VCC: Connect the VCC pin to the 3.3V power pin on the Raspberry Pi.
	- DATA: Connect the DATA pin to a digital input pin on the Raspberry Pi. You can use any of the GPIO pins on the Raspberry Pi for this purpose.we use GPIO 4(or Physical/Board pin 7)
	- GND: Connect the GND pin to a GND pin on the Raspberry Pi.
		
		Connect the Pins as Shown in [Fig.](https://drive.google.com/file/d/1m0yiuTQEp4Z-6XGbDN6aMcO2siE6_f8E/view?usp=sharing "Fig.")
2. Git clone the worker branch 

3. Install the libraries using command : 

		sudo pip install gspread oauth2client flask numpy pandas pickle scikit-learn pymongo

4. Download Google Auth.json file from Google-auth.json and place this file in the scripts folder. This file will allow you to read and write into google sheets using Google Sheets API.

### Folder Structure :
The worker node consists of following files and folders : 
**Adfruit_Python_DHT:** Consists of Sensors data reading files and collection of data to google sheets using google api.
**csv/ :**  Contains csv files for ML model training.  Book2.csv was used to train the model.
**ml code/ :** Contains code for ML model in both .ipynb and .py files

**script/ :**  Consists of all the functions for the application created in the form of different files
- 	Error404.py:  Python file which handles the functionality of 404 (Page Not Found) Page.
- 	csvAppend.py: Python file which handles the functionality of writing into a csv file.
- 	csvImport.py: Python file which handles the functionality of reading a csv file.
- 	home.py: Python file which handles the functionality of home page
- 	ip.py: Python file which handles the functionality of reading the IP address of the worker node.
- 	load.py: Python file which handles the functionality of checking the load on the worker node.
- 	login.py: Python file which handles the functionality of login page
- 	predict.py: Python file which handles the functionality of predict page
- 	 readGoogleSheet.py: Python file which handles the functionality of reading google sheets
- register.py: Python file which handles the functionality of register page
- writeToGs.py: Python file which handles the functionality of writing to google sheets
	
**static/css/ :** Contains styles.css which handles the styling of web pages

**templates/:** Contains templates for different pages of the application

- 404.html: html page template for 404 page
- home.html: html page template for home page
- loadOnWorker.html: html page template for load on worker page.
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

To get the predictions click on Predictions Button. You will be redirected to the login page. Login onto the application using credentials: 

Email: worker1@gmail.com

Password: worker1

After logging in successfully you can view the current temperature and humidity with the prediction Rain Today.
You can view the past predictions by clicking on the History button on the navbar.

