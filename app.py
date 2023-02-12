from flask import Flask, request
from flask import jsonify
import json
import requests
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast


#creating a app instance 
app = Flask(__name__)
api = Api(app)

class BankList(Resource):
    def get(self):
        url = 'https://raw.githubusercontent.com/Amanskywalker/indian_banks/main/bank_branches.csv'
        df = pd.read_csv(url, index_col=0)
        df = df.to_dict()
        return {'df' : df}, 200

# api.com/banklist
api.add_resource(BankList, '/banklist')

@app.route("/")
def home():
    return "Hello World"
    
#run the app automatically
if __name__ == "_main_":
    app.run(debug=True)