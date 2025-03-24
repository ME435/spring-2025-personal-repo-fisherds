import flask

app = flask.Flask(__name__)

@app.get("/")
def hello_anything_unique_that_you_want():
    return "Hello World!!!!"

app.run(host="0.0.0.0", port=8080, debug=True)
