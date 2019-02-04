from flask import Flask
from flask_restful import Resource, Api, reqparse
import werkzeug

# from verify_face import verify_face


app = Flask(__name__)
api = Api(app)

# parser = reqparse.RequestParser()
# parser.add_argument('face')

class FaceRecognition(Resource):

    def get(self):
        pass
        # parse = reqparse.RequestParser()
        # parse.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files')
        # args = parse.parse_args()
        # print(args)
        # audioFile = args['image']
        # print(audioFile)
        # return {'hello': 'world'}
    
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()
        face_image = args['image']
        face_image.save('temp.jpg')

        # matching_user = verify_face('temp.jpg')
        # f = open('temp.jpg', 'w')
        # f.write(face_image)
        # audioFile.save("image.jpg")


##
## Actually setup the Api resource routing here
##
api.add_resource(FaceRecognition, '/')


if __name__ == '__main__':
    app.run(debug=True)