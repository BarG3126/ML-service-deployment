"""
This module provides functionalities to load data from a database.

Includes a function to extract the RentApartments table in the db
and load it onto a pandas dataframe. This module is usefull for
scenarios where data need to be retrieved from a database for further
analysis or processing. It uses SQLAlchemy for executng DB queries
and pandas for handling the data in a DataFrame format.
"""
import pandas as pd
from loguru import logger
from sqlalchemy import select

from config import engine
from db.db_model import RentApartments


def load_data_from_db() -> pd.DataFrame:
    """
    Extract the entire RentApartments table from DB.

    Returns:
        pd.DataFrame: DataFrame containing the RentApartments data.
    """
    logger.info('extracting the table from database')
    query = select(RentApartments)
    return pd.read_sql(
        query,
        engine,
    )
