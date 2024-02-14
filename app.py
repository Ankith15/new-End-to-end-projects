from flask import Flask,request,render_templet
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
application = Flask(__name__)
app= application

## Route for Home page
@app.route('/')
def index():
    return render_templet('index.html')
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    