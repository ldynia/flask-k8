from flask import jsonify
from flask_classful import FlaskView
from flask_classful import route


class HealthView(FlaskView):

    view = 'HealthView'
    route_base = '/health'

    @route('/ready', methods=['GET'])
    def ready(self):
        return jsonify({
            'status': 'ready',
            'success': True
        }), 200

    @route('/alive', methods=['GET'])
    def alive(self):
        return jsonify({
            'status': 'alive',
            'success': True
        }), 200
