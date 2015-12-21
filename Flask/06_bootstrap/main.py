from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

# Make sure to install 'Flask-Bootstrap'
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
