import os

from flask import jsonify
from flask_classful import FlaskView
from flask_classful import route
from redis.exceptions import ConnectionError

from app import redis_cli


class HealthView(FlaskView):

    view = 'HealthView'
    route_base = '/health'

    @route('/alive', methods=['GET'])
    def alive(self):
        return jsonify({
            'status': 'alive',
            'success': True
        }), 200

    @route('/ready', methods=['GET'])
    def ready(self):
        try:
            success = True
            STATUS_CODE = 200
            redis_cli.ping()
        except ConnectionError:
            success = False
            STATUS_CODE = 504

        return jsonify({
            'status': 'ready',
            'success': success
        }), STATUS_CODE
