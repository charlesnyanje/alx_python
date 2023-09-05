#!/usr/bin/python3
"""Write a script that starts a Flask web application.
"""


from flask import Flask
"""Initialize app.
"""
app = Flask(__name__)
"""routes definition.
"""

@app.route("/")
def home():
    return "<p>Hello HBNB!</P>"

if __name__ == "__main__":
    app.run(debug=True)