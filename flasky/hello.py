from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World!</h1>"


# Dynamic components use string by default.
@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)

# Flask supports the types string, int, float, and path for routes. The path type is a special string type that can include forward slashes, unlike the string type.
@app.route("/id/<int:uid>")
def id(uid):
    return "<h1>Hello, ID {}!</h1>".format(uid)
