from flask import Flask


def create_app(config=None):

    app = Flask(__name__, static_folder=None)

    register_views(app)

    return app


def register_views(app):
    from app.modules.health.health_view import HealthView

    HealthView.register(app)