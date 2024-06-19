"""
Provides functunality for menaging ML model.

Contains ModelService class, which handles loading and using
a pre-trained ML model. The class offers methods to load a model
from a file / building a model if it doesnt exists and make predictions
using the loaded model.
"""

import pickle as pk
from pathlib import Path

from loguru import logger

from config import model_settings
from model.pipeline.model import build_model


class ModelService:
    """
    A service class for managing ML model.

    This class frovides functunalities to load a model from a specific
    path, build it if it doesnt exist and make predictions.

    Attributes:
        model: ML model menaged by this service. Initially set to None.

    Methods:
        __init__: constructor that initialize model service.
        load_model: Load model from file / build it if it doesnt exist.
        predict: makes a prediction using loaded model.
    """

    def __init__(self) -> None:  # noqa: D107
        self.model = None

    def load_model(self) -> None:
        """Load model from a specific path & build a model if doesnt exist."""
        logger.info(
            'checking the existance of model config file at: ' +
            f'{model_settings.model_path}/{model_settings.model_name}',
        )

        model_path = Path(
            f'{model_settings.model_path}/{model_settings.model_name}',
        )

        if not model_path.exists():
            logger.warning(
                f'model at: {model_path} was not found. --> ' +
                f'building {model_settings.model_name}',
            )
            build_model()

        logger.info(
            f'Model:"{model_settings.model_name}" exists -> ' +
            'loading model configuration file.',
        )

        with open(model_path, 'rb') as model_file:
            self.model = pk.load(model_file)

    def predict(self, input_parameters: list) -> list:
        """
        Make a prediction using loaded model.

        Takes input parameters and passes it to the
        model loaded using pickle file.

        Args:
            input_parameters (list): Input data for making prediction.

        Returns:
            list: The predition result from this model.
        """
        logger.info('making prediction')
        return self.model.predict([input_parameters])
