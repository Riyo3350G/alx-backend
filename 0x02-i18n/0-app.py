#!/usr/bin/env python3
""" Basic Flask app Module """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Display Hello HBNB! """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
