import lis
import subprocess
import json
from flask import Flask, request
import connect

l=lis.list()
f = open("./input.json")
data = f.read()
f.close()
app = Flask(__name__)

@app.route("/list")
def index():
        l.getcmd()
        f = open("./input.json")
        data = f.read()
        f.close()
        return data
@app.route("/connect", methods=["POST"])
def try_connct():
    connect.con(request.form['id'],request.form['pass'])
    return "ok"

app.run()
