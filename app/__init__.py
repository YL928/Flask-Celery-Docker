import os
from flask import Flask
from .settings import DevConfig, ProdConfig

if os.getenv("FLASK_ENV") == 'prod':
    DefaultConfig = ProdConfig
else:
    DefaultConfig = DevConfig
from celery import Celery
celery = Celery(__name__,backend=DevConfig.CELERY_BROKER_URL, broker=DevConfig.CELERY_BROKER_URL)
def create_app():
    if os.getenv("FLASK_ENV") == 'prod':
        DefaultConfig = ProdConfig
    else:
        DefaultConfig = DevConfig
    app = Flask(__name__)
    app.config.from_object(DefaultConfig)
    celery.conf.update(app.config)
    registe_extensions(app)
    register_blueprints(app)

    @app.route('/', methods=["get"])
    def index():
        return "It's work!"
    return app


def registe_extensions(app):
    pass


def register_blueprints(app):
    from .api import api_blueprint
    app.register_blueprint(api_blueprint)