from flask import Flask, render_template, jsonify, Response, request
import sys
import json

app = Flask(__name__)

app.debug = True

def fizz_buzz(num):
    # This is a single line, so it's an atomic operation.
    return list(map(lambda i:"FizzBuzz"[i*i%3*4:8--i**4%5] or i, range(1, num + 1)))

@app.route("/")
def index():
    return render_template("index.html", data="")

@app.route("/api/v1")
@app.route("/api/v1/<index>")
def data(index):
    return Response(json.dumps({'payload': fizz_buzz(int(index))}), mimetype='application/json')

@app.route("/fbaas")
@app.route("/fbaas/<index>")
def cool(index):
    return render_template("index.html", data=str({'payload': fizz_buzz(int(index))}))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
