from flask import Flask, Response
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route("/put", methods=['PUT'])
def put():
    response = make_response("", 530)
    return response 