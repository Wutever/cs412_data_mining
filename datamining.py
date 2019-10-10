import json
import os

from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/apriori')
def apriori():
    print("Hello")
    with open(os.path.join(os.getcwd(),"parsed1.json"),"r") as file:
        data = json.load(file)
    return data

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

    return app.send_static_file('index.html')


@app.route('/index')
def root():
    return app.send_static_file('index.html')
