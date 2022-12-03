from flask import Flask, request

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

# Flask uses contexts to temporarily make certain objects globally accessible, like request.
# The request object could be sent as an argument, but that would require every single view function in the application to have an extra parameter.
@app.route('/user-agent')
def user_agent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)
