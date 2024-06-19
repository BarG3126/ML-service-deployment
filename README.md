
# ML Service for Rental Apartment Analysis

## Overview

This repository contains a machine learning service designed to process and analyze rental apartment data. The service uses advanced machine learning techniques to provide insights and predictions. It is built with Python and structured using Poetry for dependency management.

## Features

- Data processing and cleaning
- Machine learning model training and evaluation
- Prediction generation
- Logging and configuration management

## Project Structure

```
Deployment/
├── Makefile
├── poetry.lock
├── pyproject.toml
├── rent_apartments.csv
├── setup.cfg
└── src/
    ├── config/
    ├── db/
    ├── logs/
    ├── model/
    │   ├── model_service.py
    │   ├── models/
    │   │   ├── rf_db_v1
    │   │   └── rf_db_v2
    │   └── pipeline/
    │       ├── collection.py
    │       ├── model.py
    │       └── preperation.py
    └── runner.py
```

- **Makefile**: Contains commands for setting up and running the project.
- **poetry.lock**: Lock file for Poetry dependencies.
- **pyproject.toml**: Configuration file for Poetry and project dependencies.
- **rent_apartments.csv**: Dataset containing rental apartment information.
- **setup.cfg**: Configuration file for setup tools.
- **src/**: Directory containing the source code.
  - **config/**: Configuration files and settings.
  - **db/**: Database-related code.
  - **logs/**: Logging setup and log files.
  - **model/**: Machine learning model code.
    - **model_service.py**: Main service script for model operations.
    - **models/**: Directory containing trained model versions.
      - **rf_db_v1**: First version of the random forest model.
      - **rf_db_v2**: Second version of the random forest model.
    - **pipeline/**: Data processing and model pipeline scripts.
      - **collection.py**: Script for data collection.
      - **model.py**: Script defining the model architecture.
      - **preperation.py**: Script for data preparation.
  - **runner.py**: Main script to run the ML service.

## Installation

1. Clone the repository:

   ```sh
   git clone <repository_url>
   cd <repo location>
   ```

2. Install dependencies using Poetry:

   ```sh
   poetry install
   ```

3. Run the setup commands:

   ```sh
   make setup
   ```

## Usage

1. To start the service, run:

   ```sh
   poetry run python src/runner.py
   ```

2. The service will read the dataset, process the data, train the model, and generate predictions.

## Configuration

Configuration settings are located in the `src/config` directory. Adjust the settings as needed to match your environment and requirements.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
