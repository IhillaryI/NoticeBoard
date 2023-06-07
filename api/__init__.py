#!/usr/bin/env python3

from os import environ
from flask import Flask, make_response, jsonify, render_template
from flask_cors import CORS
from models import storage


def create_app():
    app = Flask(__name__)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

    @app.teardown_appcontext
    def close_db(error):
        storage.close()

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': "Not found"}), 404)

    @app.errorhandler(400)
    def bad_request(error):
        return make_response(jsonify({'error': error.description}), 400)

    @app.route('/hello')
    def hello():
        return 'Hello, world!'

    from api.v1 import (users, notice)
    app.register_blueprint(users.bp)
    app.register_blueprint(notice.bp)


    return app


if __name__ == '__main__':
    host = environ.get('API_HOST')
    port = environ.get('API_PORT')

    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5001'

    app = create_app()
    app.run(host=host, port=port)
