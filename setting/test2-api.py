from flask import Flask, request
from flask.ext.cors import  CORS
app = Flask(__name__)
cors=CORS(app)
f = open("./input.json")
data = f.read()
f.close()
@app.route("/list",methods=["GET"])
def index():
    print("list request")
    return data
@app.route("/connect_app", methods=["POST"])
def try_connct():
    app_data = request.data
    a = app_data.decode()
    p = open("./pass.txt", "w")
    p.write(a)
    p.close
    print("connect request",a)
    return "ok"
app.run(host="0.0.0.0")
