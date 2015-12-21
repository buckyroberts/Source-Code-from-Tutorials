from flask import Flask, request

app = Flask(__name__)


# Flask can respond differently to various HTTP methods
@app.route("/")
def index():
    return "Method used: %s" % request.method


# By default only GET allowed, but you can change that using the methods argument
@app.route("/bacon", methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are probably using GET"


if __name__ == "__main__":
    app.run()
