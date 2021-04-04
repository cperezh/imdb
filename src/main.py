from flask import Flask
import pickle as pkl
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def predict_film():
    
    print(os.getcwd())
    model = pkl.load(open("./src/mdb_class.pkl", "rb"))

    X = [[2092354, 2010, 148 ]]

    print(model.predict(X))
    print("hola")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

if __name__ == "__main__":
    predict_film()