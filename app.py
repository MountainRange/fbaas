from flask import Flask, render_template, jsonify, Response, request
import sys
import json

app = Flask(__name__)

app.debug = True


@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/test")
@app.route("/test/<index>")
def data(index):
	return Response({'Hello':'World'}, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
