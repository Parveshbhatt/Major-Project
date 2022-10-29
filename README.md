# Major-Project
## Environmental Condition monitoring system based on edge-fog computing using machine learning



## Setup

 ML model requires [Python](http://www.python.org//) and Flask to run.

Install the dependencies and start the server.

```sh
pip install flask
python app.py
```


## Development
### Folder Structure:
#### Models:
Contains Pickle file for all the models consisting of Logistic Regression, Random Forest, SVM, Decision Tree packed in the form of .pkl files 
#### Template: 
Contains an HTML file for inputing the data through web interface and displaying the result on the web page

#### static/css:
Contains css file for the index.html

#### Major_Project.py
It is the Python file for the ML model

#### Major_Project.ipynb
It is the Jupyter notebook for the ML model, contains all the code for vizualization and training of the dataset

#### app.py
It is the server file used to render data on index.html and to process the data passed through the html file to the ml model. It acts as an interface between the web interface and the ml model

#### Weather1.csv
It is the dataset used for the training of the model
