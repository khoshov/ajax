import json
from flask import request
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/say/hello', methods=['POST'])
def say_hello():
    data = request.json
    first_name = data.get('first_name')
    return json.dumps({'message': f'What\'s up {first_name.upper()}'})


if __name__ == '__main__':
    app.run()
