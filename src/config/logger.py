"""
This module sets up the logging configuration.

Using Pydantic BaseSettings for configuration argument,
allowing settings to be read from environ variables and .env file.
"""

from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggerSettings(BaseSettings):
    """
    Configuration log level settings.

    Attributes:
        model_config (SettingsConfigDict): Model config, loaded from .env file.
        log_level (str): Logging level of the app.
    """

    model_config = SettingsConfigDict(
        env_file='config/.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )

    log_level: str


def configure_logging(log_level: str) -> None:
    """
    Configure the logging for the app.

    Args:
        log_level (str): The log level to be set to the logger.
    """
    logger.remove()  # so logs won't be displayed on the console
    logger.add(
        'logs/app.log',
        rotation='1 day',
        retention='2 days',
        compression='zip',
        level=log_level,
    )


configure_logging(log_level=LoggerSettings().log_level)
