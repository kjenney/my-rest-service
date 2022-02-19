from flask import Flask
from flask import request
from flask import jsonify
import datetime

startTime = datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S")

app = Flask(__name__)

@app.route("/")
def show_details() :
    global startTime
    return "<html>" + \
           "<head><title>K8S + Flask Demo</title></head>" + \
           "<body>" + \
           "<table>" + \
           "<tr><td> Start Time </td> <td>" +  startTime + "</td> </tr>" \
           "<tr><td> Remote Address </td> <td>" + request.remote_addr + "</td> </tr>" \
           "</table>" + \
           "</body>" + \
           "</html>"

@app.route("/json")
def send_json() :
    global startTime
    return jsonify( {'StartTime' : startTime,
                     'RemoteAddress':  request.remote_addr} )

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')
