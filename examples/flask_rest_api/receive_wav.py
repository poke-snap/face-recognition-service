from flask import Flask
from flask_restful import Resource, Api, reqparse
import werkzeug


class UploadWavAPI(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('audio', type=werkzeug.FileStorage, location='files')

        args = parse.parse_args()

        stream = args['audio'].stream
        wav_file = wave.open(stream, 'rb')
        signal = wav_file.readframes(-1)
        signal = np.fromstring(signal, 'Int16')
        fs = wav_file.getframerate()
        wav_file.close()