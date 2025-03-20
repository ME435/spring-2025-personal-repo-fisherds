import flask
from plateloader import PlateLoader
import threading

app = flask.Flask(__name__,
            static_url_path='',
            static_folder='public')

serial_lock = threading.Lock()

@app.get("/")
def handle_naked_domain():
    return flask.redirect("/index.html")

@app.route('/api/<command>')
def api_command(command):
    with serial_lock:
        plateLoader = PlateLoader()
        plateLoader.connect("/dev/ttyACM0")
        response = plateLoader.send_command(command)
        plateLoader.disconnect()  # Good do do this.
    return response
    # print(f"Got the request {command}")
    # return f"TODO send {command}"
    

app.run(host='0.0.0.0', port=8080, debug=True)