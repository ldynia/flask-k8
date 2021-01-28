import os
import socket

from flask import jsonify

from app.run import app


@app.route('/')
def hello_app():
    return jsonify({
        'data': 'Hello REST API!',
        'app': os.getenv('APP_COLOR'),
        'hostname': socket.gethostname(),
    }), 200
