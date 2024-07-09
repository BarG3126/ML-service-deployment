"""
Main application script for running the ML model service.

This script initialize the ModelService, loads the ML model,
makes a prediction based on predifined input parameters and log
the output. Demonstrates the typical workflow of using the ModelService
in a practical application context.
"""

from loguru import logger

from model.model_service import ModelService


@logger.catch
def main():
    """
    Run the apllication.

    Load the model, make a prediction based on provided data
    and log the prediction
    """
    logger.info('running the application...')
    ml_svc = ModelService()
    ml_svc.load_model()

    feature_values = {
        'area': 85,
        'constraction_year': 2015,
        'bedrooms': 2,
        'garden_area': 20,
        'balcony_present': 1,
        'parking_present': 1,
        'furnished': 0,
        'garage_present': 0,
        'storage_present': 1,
    }

    pred = ml_svc.predict(list(feature_values.values()))
    logger.info(f'prediction = {pred}')


if __name__ == '__main__':
    main()
