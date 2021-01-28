import os
import socket

from flask import jsonify

from app.run import app


@app.route('/app')
def hello_app():
    return jsonify({
        'app': os.getenv('APP_COLOR'),
        'hostname': socket.gethostname(),
    }), 200
