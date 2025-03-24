import flask

app = flask.Flask(__name__)

@app.route("/")
def hello_anything_you_want():
    return "Hello World!!!!"

app.run(host="0.0.0.0", port=8080, debug=True)
