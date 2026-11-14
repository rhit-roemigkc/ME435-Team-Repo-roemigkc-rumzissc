import flask
import datetime

app = flask.Flask(__name__, static_url_path="", static_folder="public")

@app.get("/api/<username>/<message>")
def handle_message(username, message):
    
    return

@app.route("/")
def naked_domain_route():
    return flask.redirect("/index.html")

if __name__ == "__main__":
    print("Running flask!")
    app.run(host="0.0.0.0", port=8081, debug=True, use_reloader=True)