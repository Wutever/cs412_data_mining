import json
import os

from flask import Flask, escape, request

from apriori import processData

from dbscan import dbscan1
from user_case1 import pieChart
from user_case2 import user_case2

app = Flask(__name__)

csv_file = os.path.join(os.getcwd(), "parsed1.json")
csv_file2 = os.path.join(os.getcwd(), "netherlands.json")
csv_file3 = os.path.join(os.getcwd(), "united_kingdom.json")
csv_file4 = os.path.join(os.getcwd(), "france.json")
csv_file5 = os.path.join(os.getcwd(), "spain.json")
csv_file6 = os.path.join(os.getcwd(), "italy.json")
csv_file7 = os.path.join(os.getcwd(), "austria.json")

index = "hotel_cleaned.csv"

@app.route('/getjson')
def getjson():

    return ""


@app.route('/apriori', methods=['POST'])
def apriori():
    support = request.values["Support in Ratio"]
    itemSize = request.values["Maximum Item Set"]
    column = request.values["Columns"]

    return processData(float(support), int(itemSize), column.split(","), index)


@app.route('/usercase2', methods=['POST'])
def user_casetwo():
    tmp = {}
    for key in request.values.dicts[1] :
        if key == 'info':
            info = request.values.dicts[1][key]
            continue
        tmp[key] = request.values.dicts[1][key].split("|")

    return user_case2(tmp,info.split(","),index)

@app.route('/dbscan', methods=['POST'])
def dbscan():

    tmp = {}
    for key in request.values.dicts[1] :
        if key == 'factor':
            second = request.values.dicts[1][key]
            continue
        if key == 'eps':
            eps =  request.values.dicts[1][key]
            continue
        if key == 'minpts':
            minpts =  request.values.dicts[1][key]
            continue
        tmp[key] = request.values.dicts[1][key].split("|")
    return dbscan1(tmp, second, int(eps), int(minpts), index)

@app.route('/piechart', methods=['POST'])
def piechart():

    tmp = {}
    for key in request.values.dicts[1] :
        if key == 'second':
            second = request.values.dicts[1][key]
            continue
        tmp[key] = request.values.dicts[1][key].split("|")

    return pieChart(tmp, second, index)


@app.route('/start')
def start():
    with open(csv_file, "r") as file:
        data = json.load(file)
    return data


@app.route('/netherlands')
def netherlands():
    with open(csv_file2, "r") as file:
        data = json.load(file)
    return data


@app.route('/united_kingdom')
def united_kingdom():
    with open(csv_file3, "r") as file:
        data = json.load(file)
    return data


@app.route('/france')
def france():
    with open(csv_file4, "r") as file:
        data = json.load(file)
    return data


@app.route('/spain')
def spain():
    with open(csv_file5, "r") as file:
        data = json.load(file)
    return data


@app.route('/italy')
def italy():
    with open(csv_file6, "r") as file:
        data = json.load(file)
    return data


@app.route('/austria')
def austria():
    with open(csv_file7, "r") as file:
        data = json.load(file)
    return data


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/index')
def root():
    return app.send_static_file('index.html')


@app.route('/updateIndex', methods=['POST'])
def updateindex():
    tmp = {}
    for key in request.values.dicts[1] :
        tmp[key] = request.values.dicts[1][key]
    global index
    index = tmp["index"] + ".csv"

    return "finish"
