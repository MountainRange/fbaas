from flask import Flask, render_template, jsonify, Response, request
import sys
import json

app = Flask(__name__)

app.debug = True

def fizz_buzz(num):
    # This is a single line, so it's an atomic operation.
    return list(map(lambda x: "FizzBuzz" if x % 3 == 0 and x % 5 == 0 \
        else ("Fizz" if x % 3 == 0 else("Buzz" if x % 5 == 0 else x)), range(1, num + 1)))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
@app.route("/test/<index>")
def data(index):
    return Response(json.dumps({'data': fizz_buzz(int(index))}), mimetype='application/json')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
