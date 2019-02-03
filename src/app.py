#!flask/bin/python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/face-recognition/api/v1.0/image', methods=['POST'])
def receive_image():


if __name__ == '__main__':
    app.run(debug=True)