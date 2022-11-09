#!/usr/bin/python3
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """ Function called with / route """
    name = request.args.get("name", "World")
    return f'Hello HBNB!, {escape(name)}!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
