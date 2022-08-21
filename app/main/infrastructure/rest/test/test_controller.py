from flask import Blueprint

blueprint = Blueprint('test_module', __name__)
blueprint_base = '/test'


@blueprint.route('index', methods=["GET"])
def index():
    """
    Test blueprint by loading <base_url>/<app_prefix>/<blueprint_base>/<route_name>
    http://127.0.0.1:5000/api/v1/test/index
    :return:
    """
    return 'Hello from test module', 200
