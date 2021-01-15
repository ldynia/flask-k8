import os
import redis

from flask import Flask

REDIS_DB = os.getenv('REDIS_DB', 0)
REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)

redis_cli = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


def create_app(config=None):
    app = Flask(__name__, static_folder=None)

    register_views(app)

    return app


def register_views(app):
    from app.modules.health.health_view import HealthView

    HealthView.register(app)