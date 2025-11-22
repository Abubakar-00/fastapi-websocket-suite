import os


class Config:
    """
    Application configuration loaded from environment variables.
    """

    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


config = Config()
