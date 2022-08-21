from dotenv import load_dotenv

from app.main.infrastructure import start_app

load_dotenv()

app = start_app()


def handle_async_request(event, context):
    """
    Handles request from queues and schedulers
    :param event:
    :param context:
    :return:
    """
