"""
This module sets up the database configuration.

Using Pydantic BaseSettings for configuration argument,
allowing settings to be read from environ variables and .env file.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine


class DataBaseSettings(BaseSettings):
    """
    Database configuration for the app.

    Attributes:
        model_config (SettingsConfigDict): Model config loaded from .env file.
        rent_apart_table_name (str): Name of the table in the DB.
        db_conn_str (str): Database connection string.
    """

    model_config = SettingsConfigDict(
        env_file='config/.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )

    rent_apart_table_name: str
    db_conn_str: str


database_settings = DataBaseSettings()


engine = create_engine(database_settings.db_conn_str)
