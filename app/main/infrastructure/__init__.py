import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy as _BaseSQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_injector import FlaskInjector

from app.main.infrastructure.config import config_by_name
from app.main.infrastructure.dependencies import configure
from app.main.infrastructure.rest import register_blueprints


# Taken from https://github.com/pallets/flask-sqlalchemy/issues/589#issuecomment-361075700
class SQLAlchemy(_BaseSQLAlchemy):
    def apply_pool_defaults(self, app, options):
        super(SQLAlchemy, self).apply_pool_defaults(app, options)
        options["pool_pre_ping"] = True


db = SQLAlchemy()
db.session.expire_on_commit = False

marshmallowConfig = Marshmallow()


def create_app(config_name):
    app = Flask(__name__)
    environment_config = config_by_name[config_name]
    app.config.from_object(environment_config)

    Migrate(app, db)
    db.init_app(app)
    marshmallowConfig.init_app(app)

    return app


def setup_dependency_injection(app, injector_configuration_function):
    FlaskInjector(app=app, modules=[injector_configuration_function])


def start_app():
    environment = os.getenv('FLASK_ENV') or 'development'
    app = create_app(environment)

    api_prefix = "/api/v1"
    register_blueprints(app, api_prefix)

    # Add some decorators
    @app.route(api_prefix + '/')
    def hello_world():
        """ hello world """
        return 'Hello, World!'

    @app.after_request
    def apply_cors(response):
        """ applies cors to all requests """
        response.headers['Access-Control-Allow-Origin'] = app.config['ORIGIN']
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, PUT, POST, DELETE, OPTIONS'
        return response

    setup_dependency_injection(app, configure)

    return app
