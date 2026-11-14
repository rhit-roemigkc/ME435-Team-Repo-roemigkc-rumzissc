import flask
import time
import threading
app = flask.Flask(__name__, static_url_path="", static_folder="public")
 
messages = []
lock = threading.Lock()
 
@app.post("/send")

def send():

    data = flask.request.get_json(silent=True)
    username = str(data.get("username", "")).strip()
    text = str(data.get("text", "")).strip()

    with lock:
        messages.append({
            "id": len(messages) + 1,
            "username": username,
            "text": text,
            "time": int(time.time() * 1000),
        })

    return flask.jsonify(ok=True)
 
@app.get("/messages")
def get_messages():
    after = flask.request.args.get("after", 0, type=int)
    with lock:
        return flask.jsonify(messages[after:])
 
@app.route("/")
def naked_domain_route():
    return flask.redirect("/index.html")
 
if __name__ == "__main__":
    print("Running flask!")
    app.run(host="0.0.0.0", port=8081, debug=True, use_reloader=True)