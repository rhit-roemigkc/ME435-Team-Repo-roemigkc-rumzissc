import flask

app = flask.Flask(__name__, static_url_path="", static_folder="public")


@app.get("/api/hello/<name>")
def hello_name(name):
    return f"Hello, {name}!"

@app.route("/")
def naked_domain_route():
    return f"Hello, Val!"


if __name__ == "__main__":
    print("Running flask!")
    app.run(host="0.0.0.0", port=8080, debug=True)#, use_reloader=False)
