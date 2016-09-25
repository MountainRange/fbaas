from flask import Flask, render_template, Response
import json
import time

app = Flask(__name__)

app.debug = True

def fizz_buzz(num):
    # This is a single line, so it's an atomic operation.
    return list(map(lambda i:"FizzBuzz"[i*i%3*4:8--i**4%5] or str(i), range(1, num + 1)))

@app.route("/")
def index():
    return render_template("index.html", data="")

@app.route("/api/v1")
@app.route("/api/v1/<index>")
def data(index):
    return Response(json.dumps({'payload': fizz_buzz(int(index)), 'response': '200 OK',
                                'time': time.time(),
                                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.7.0 Chrome/49.0.2623.111 Safari/537.36',
                                'server-load': 0.0, 'response-time': 0.0}),
                    mimetype='application/json')

@app.route("/fbaas")
@app.route("/fbaas/<index>")
def cool(index):
    return render_template("index.html", data=str({'payload': fizz_buzz(int(index))}))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
