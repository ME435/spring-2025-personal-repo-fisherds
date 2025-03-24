import flask

app = flask.Flask(__name__)

@app.route("/api/<command>")
def api_command(command):
    return f"Hello, {command}!"

app.run(host="0.0.0.0", port=8080, debug=True)
