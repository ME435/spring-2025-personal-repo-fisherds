import flask

app = flask.Flask(__name__,
                  static_url_path="",
                  static_folder="public")

@app.get("/")
def naked_domain_redirect():
    return flask.redirect("index.html")


@app.route("/api/<command>")
def api_command(command):
    return f"TODO: Actually send the commnd: {command}"


app.run(host="0.0.0.0", port=8080, debug=True)
