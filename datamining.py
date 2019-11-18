import json
import os

from flask import Flask, escape, request

from apriori import processData

app = Flask(__name__)

csv_file = os.path.join(os.getcwd(), "parsed1.json")


@app.route('/getjson')
def getjson():

    return ""


@app.route('/apriori', methods=['POST'])
def apriori():
    support = request.values["Support in Ratio"]
    itemSize = request.values["Maximum Item Set"]
    column = request.values["Columns"]

    return processData(float(support), int(itemSize), column.split(","))

@app.route('/kmeans', methods=['POST'])
def kmeans():
    data = []
    for value in request.values.values():
        data.append(value)
    return


@app.route('/start')
def start():
    with open(csv_file, "r") as file:
        data = json.load(file)
    return data


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/index')
def root():
    return app.send_static_file('index.html')
