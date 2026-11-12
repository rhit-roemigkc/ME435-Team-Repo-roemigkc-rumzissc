import flask

app = flask.Flask(__name__, static_url_path="", static_folder="public")
usernames = []
messages = []
counter = 1

@app.get("/api/<username>/<message>")
def handle_message(username, message):
    if counter >= 21:
        for i in range(start = 1, stop = 19,step = 1):
            usernames[i] = usernames[i+1]
            messages[i] = messages[i+1]
        usernames[20] = username
        messages[20] = message
    else:
        usernames[counter] = username
        messages[counter] = message
        counter = counter + 1
    return

@app.route("/")
def naked_domain_route():
    return flask.redirect("/index.html")


if __name__ == "__main__":
    print("Running flask!")
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)
