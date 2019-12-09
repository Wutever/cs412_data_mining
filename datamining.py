import json
import os

from flask import Flask, escape, request

from apriori import processData

from dbscan import dbscan1
from user_case1 import pieChart

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

@app.route('/dbscan', methods=['POST'])
def dbscan():

    tmp = {}
    for key in request.values.dicts[1] :
        if key == 'factor':
            second = request.values.dicts[1][key]
            continue
        tmp[key] = request.values.dicts[1][key].split("|")
    return dbscan1(tmp, second)

@app.route('/piechart', methods=['POST'])
def piechart():

    tmp = {}
    for key in request.values.dicts[1] :
        if key == 'second':
            second = request.values.dicts[1][key]
            continue
        tmp[key] = request.values.dicts[1][key].split("|")

    return pieChart(tmp, second)


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
