import flask

app = flask.Flask(__name__)

@app.route('/api/hello/<name>')
def hello_name(name):
    return f'Hello, {name}!'

app.run(host='0.0.0.0', port=8080, debug=True)