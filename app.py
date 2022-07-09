from unittest import result
from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# define some route 
@app.route("/bot", method = ["POST"])

#reponse
def response():
    query = dict(request.form)['query']
    result = query + " " + time.ctime()
    return jsonify({"response" : result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", )