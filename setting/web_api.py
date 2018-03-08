from flask import Flask, request
from flask.ext.cors import  CORS
app = Flask(__name__)
cors=CORS(app)
f = open("./home/pi/RasPi-server/settong/input.json")
data = f.read()
f.close()

@app.route("/list",methods=["GET"])
def index():
    return data

@app.route("/connect", methods=["POST"])
def try_connect():
    ssid = request.form['ssid']
    password = request.form['pass']
    writepass(ssid + " " + password)
    return "ok"

@app.route("/connect_app", methods=["POST"])
def try_conncet_app():
    app_data = request.data
    writepass(app_data.decode())
    return "ok"

def writepass(st):
    p = open("./home/pi/RasPi-client/setting/pass.txt", "w")
    p.write(st)
    p.close()

app.run(host="0.0.0.0")
