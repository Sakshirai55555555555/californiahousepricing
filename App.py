import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__) #this initializes a Flask object where __name__ refers to the name of the current Python module.

rfmodel=pickle.load(open('rf_model.pkl','rb')) #loading the model


#This code defines a route for the home page ('/') of your web application and links it to a function named home(). When a user visits the root URL of your website, this function is called, and it renders a template named home.html using Flask's render_template function.
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict_api',methods=['POST']) #it would receive data in the POST request, process it in some way, and then potentially return a response with the results or perform some action based on the received data.

def predict_api():
    data=request.json['data'] #This function appears to be designed to handle incoming JSON data from an HTTP POST request
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=np.array(list(data.values())).reshape(1,-1) #preddicting new data
    output=rfmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0]) #convert a Python dictionary into a JSON response that can be sent back to the client

#starting the appplication
if __name__=="__main__":
    app.run(debug=True)