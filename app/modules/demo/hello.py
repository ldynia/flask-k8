import socket

from app.run import app


@app.route('/')
def hello_world():
    hostname = socket.gethostname()

    return f'Hello! Says {hostname}'
