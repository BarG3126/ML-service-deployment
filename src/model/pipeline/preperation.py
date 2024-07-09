"""
This module provides functionality for preparing a dataset for ML model.

Consists of functions to load a dataset, encode categorical columns and
parse specific columns for further processing.
"""

import re

import pandas as pd
from loguru import logger

from model.pipeline.collection import load_data_from_db


def prepare_data() -> pd.DataFrame:
    """
    Prepare the dataset for analysis and modelling.

    This involves loading the data, encoding categorical columns
    and parsing the 'garden' column.

    Returns:
        pd.DataFrame: The processed dataset.
    """
    logger.info('starting up preprocessing pipeline')
    dataframe = load_data_from_db()
    data_encoded = _encode_cat_cols(dataframe)
    return _parse_garden_col(data_encoded)


def _encode_cat_cols(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Encode categorical columns into dummy variables.

    Args:
        dataframe (pd.DataFrame): The original dataset.

    Returns:
        pd.Dataframe: The dataset with categorical columns encoded.
    """
    cols = ['balcony', 'parking', 'furnished', 'garage', 'storage']
    logger.info(
        f'encoding categorical columns: {cols}',
    )

    return pd.get_dummies(
        dataframe,
        columns=cols,
        drop_first=True,
    )


def _parse_garden_col(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Parse the 'garden' column in the dataset.

    Args:
        dataframe (pd.DataFrame): The dataset with 'garden' columns.

    Returns:
        pd.DataFrame: The dataset with the 'garden' columns parsed
    """
    logger.info('parsing garden area columns')

    def parse_garden_area(x):
        if x == 'Not present':
            return 0
        else:
            match = re.findall(r'\d+', x)
            if match:
                return int(match[0])
            else:
                return 0  # or another appropriate default value

    dataframe['garden'] = dataframe['garden'].apply(parse_garden_area)
    return dataframe
