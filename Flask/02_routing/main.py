from flask import Flask

app = Flask(__name__)


# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route("/")
def hello():
    return "Home page"


# the server response is the return value of the function
@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good</h2>'


# Display variable using <variable_name>
@app.route('/user/<username>')
def show_user_profile(username):
    return 'Hey there %s' % username


# To use int or float <converter:variable_name>
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post id: %d' % post_id


if __name__ == "__main__":
    app.run()
