from flask import Flask, render_template

app = Flask(__name__)


# For render_template pass in name of template and any variables needed
@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', name=name)


if __name__ == "__main__":
    app.run()
