from .test.test_controller import blueprint as test_blueprint, blueprint_base


def register_blueprints(app, prefix: str):
    app.register_blueprint(test_blueprint, url_prefix=prefix + blueprint_base)
