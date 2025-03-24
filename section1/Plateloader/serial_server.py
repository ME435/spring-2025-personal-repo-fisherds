import flask
from plateloader import Plateloader
import threading

app = flask.Flask(__name__,
                  static_url_path="",
                  static_folder="public")

serial_lock = threading.Lock()

@app.get("/")
def naked_domain_redirect():
    return flask.redirect("index.html")


@app.route("/api/<command>")
def api_command(command):
    with serial_lock:
        pl = Plateloader()
        pl.connect("/dev/ttyACM0")
        resp = pl.send_command(command)
        pl.disconnect()
        return resp


app.run(host="0.0.0.0", port=8080, debug=True)
