import flask

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

app.run(host='0.0.0.0', port=8080, debug=True)

