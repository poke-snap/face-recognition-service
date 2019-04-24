import os
from os import listdir
from os.path import isfile, join, splitext

import face_recognition
from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import BadRequest

from processing import images

import boto3

# Global storage for images
faces_dict = {}

# Create flask app
app = Flask(__name__)
CORS(app)

client = boto3.client('dynamodb')


@app.route('/', methods=['POST'])
def web_recognize():
    """REST API to add new image to the server

    Example:
    curl -X POST -F file=@<filename> <hostname>:<port> 
    """
    file = images.extract_image(request)

    if file and images.is_picture(file.filename):
        # The image file seems valid! Detect faces and return the result.
        return jsonify(images.detect_faces_in_image(file, faces_dict))
    else:
        raise BadRequest("Given file is invalid!")


@app.route('/faces', methods=['GET', 'POST', 'DELETE'])
def web_faces():
    """REST API to add / retrieve faces

    Example:
    curl -X POST -F file=@<filename> <hostname>:<port>/faces?id=<id>
    """
    # GET
    if request.method == 'GET':
        return jsonify(list(faces_dict.keys()))

    # POST/DELETE
    file = images.extract_image(request)
    if 'id' not in request.args:
        raise BadRequest("Identifier for the face was not given!")

    if request.method == 'POST':
        try:
            new_encoding = images.calc_face_encoding(file)
            faces_dict.update({request.args.get('id'): new_encoding})
        except Exception as exception:
            raise BadRequest(exception)

    elif request.method == 'DELETE':
        faces_dict.pop(request.args.get('id'))

    return jsonify(list(faces_dict.keys()))


if __name__ == "__main__":
    print("Starting by generating encodings for found images...")
    # Calculate known faces
    faces_dict = images.get_faces_dict(os.getenv('FACE_RECOGNITION_SERVICE_IMAGE_FILES', 'test_images'))

    # Start app
    print("Starting WebServer...")
    app.run(host='0.0.0.0', port=8080, debug=False)
