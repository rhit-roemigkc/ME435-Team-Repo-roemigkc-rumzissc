import flask
import threading
import myPiServer

app = flask.Flask(__name__, static_url_path="", static_folder="public")

serial_lock = threading.Lock()
myServer = myPiServer.MyPiServer()


@app.get("/api/<username>/<message>")
def handle_message(username, message):
    with serial_lock:
        response = myServer.send_message(username, message)
    return response

@app.route("/")
def naked_domain_route():
    return flask.redirect("/index.html")


if __name__ == "__main__":
    print("Running flask!")
    myServer.connect()
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)
