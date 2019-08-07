from app.spoopy import create_note
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_api import status

def create_app(ConfigClass):
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(ConfigClass)

    with app.app_context():

        @app.route('/', methods=['POST'])
        def get_spoopy():
            if request.form['query'] != None:
                return create_note(request.form['query'])
            else:
                content = {'error': 'invalid'}
                return content, status.HTTP_404_NOT_FOUND
    return app
