from flask import Flask, request
import pickle as pkl
import pandas as pd
import os

app = Flask(__name__)

@app.route('/predict')
def predict():
    
    num_votes = request.args.get('num_votes')
    startyear = request.args.get('startyear')
    runtimeminutes = request.args.get('runtimeminutes')
    
    return predict_film(num_votes, startyear, runtimeminutes)
 
def predict_film(num_votes, startyear, runtimeminutes):
    '''
    Returns de prediction for a film

    Parameters:
        num_votes: votes of the film in IMDB
        startyear: year it was filmed
        runtimeminutes: minutes of the film
    
    Return:
        String: the prediction Buena o Mala
    '''
    
    # Get trained model
    model = pkl.load(open("./src/mdb_class.pkl", "rb"))

    X = [[num_votes, startyear, runtimeminutes ]]

    return str(model.predict(X))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

if __name__ == "__main__":
    print(predict_film())