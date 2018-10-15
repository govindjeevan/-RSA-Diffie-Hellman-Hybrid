
from flask import Flask
app = Flask(__name__)from flask i 

@app.route("/")
def hello():
    return "Hello World!"