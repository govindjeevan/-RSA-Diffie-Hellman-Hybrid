from flask import Flask
from flask import request
import Hybrid
from flask import render_template
from flask import jsonify, json

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template("my_form.html")


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    data= Hybrid.hybrid(text)
    list = []
    for key, value in data.items():
    	list.append({key:value})
    data = jsonify(json.dumps(list))
    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run()
