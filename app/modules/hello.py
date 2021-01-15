import os
import redis
import socket

from app.config.run import app

APP = os.getenv('APP_COLOR', 'orange')
REDIS_DB = os.getenv('REDIS_DB', 0)
REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)

redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    hostname_count = visit_counter()

    return f'Hello, {APP} :) Says {hostname}! Visits: {hostname_count}'

def visit_counter():
    count = redis.get('hostname')
    if not count:
        count = 0
        redis.set('hostname', count)
    else:
        count = int(count) + 1
        redis.set('hostname', count)

    return count