import os
import socket

from app.run import app


@app.route('/app')
def hello_app():
    app = os.getenv('APP_COLOR', 'orange')
    hostname = socket.gethostname()

    return f'Hello, {app} :) Says, {hostname}!'
