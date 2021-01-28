from flask import jsonify

from app.run import app


@app.route('/')
def hello_world():
    return jsonify({
        'data': 'Hello REST API!',
    }), 200
