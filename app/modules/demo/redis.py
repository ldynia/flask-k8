import os
import socket

from flask import jsonify

from app import redis_cli
from app.run import app


@app.route('/redis')
def hello_redis():
    hostname = socket.gethostname()
    tvc, hvc = count_visits(hostname)

    return jsonify({
        'app': os.getenv('APP_COLOR'),
        'hostname': hostname,
        'host_visits_count': hvc,
        'total_visits_count': tvc,
    }), 200


def count_visits(hostname):
    total_visits_count = redis_cli.get('visits')
    if not total_visits_count:
        total_visits_count = 0
        redis_cli.set('visits', total_visits_count)
    else:
        total_visits_count = int(total_visits_count) + 1
        redis_cli.set('visits', total_visits_count)

    host_visits_count = redis_cli.get(hostname)
    if not host_visits_count:
        host_visits_count = 0
        redis_cli.set(hostname, host_visits_count)
    else:
        host_visits_count = int(host_visits_count) + 1
        redis_cli.set(hostname, host_visits_count)

    return total_visits_count, host_visits_count
