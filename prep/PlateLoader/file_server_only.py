import flask

app = flask.Flask(__name__,
            static_url_path='',
            static_folder='public')

@app.get("/")
def handle_naked_domain():
    return flask.redirect("/index.html")

app.run(host='0.0.0.0', port=8080, debug=True)