import logging

from server.config import config


def setup_logging():
    """
    Configure and return the application logger.
    """
    logging.basicConfig(
        level=config.LOG_LEVEL,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger("ws_server")


logger = setup_logging()
