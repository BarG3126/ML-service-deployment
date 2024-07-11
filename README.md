
# ML Service for Rental Apartment Analysis

## Overview

This repository contains a machine learning service designed to process and analyze rental apartment data. The service uses advanced machine learning techniques to provide insights and predictions. It is built with Python and structured using Poetry for dependency management.

## Features

- Data processing and cleaning
- Machine learning model training and evaluation
- Prediction generation
- Logging and configuration management
- CI/CD with GitHub Actions
- Modular and scalable architecture (upcoming)

## Project Structure

```
ML-service-deployment/
├── .github/
│   ├── actions/
│   │   └── build-application/
│   │       └── action.yml
│   └── workflows/
│       └── lint.yml
├── Makefile
├── poetry.lock
├── pyproject.toml
├── rent_apartments.csv
├── setup.cfg
├── README.md
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

- **.github/**: Directory for GitHub Actions workflows and actions.
  - **actions/**: Custom GitHub Actions.
    - **build-application/**: Contains `action.yml` to define the build application action.
  - **workflows/**: Contains GitHub Actions workflow definitions.
    - **lint.yml**: Workflow for linting the codebase on push or pull request events.
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
    - **pipeline/**: Data processing and model pipeline scripts.
      - **collection.py**: Script for data collection.
      - **model.py**: Script defining the model architecture.
      - **preparation.py**: Script for data preparation.
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

## CI/CD

This project uses GitHub Actions for continuous integration and continuous deployment.

- **Lint Workflow**: The lint workflow (`lint.yml`) runs on push and pull request events to the main branch. It checks out the repository, builds the application, and runs linting using Flake8.

- **Build Application Action**: The custom build application action (`action.yml`) sets up Python, installs Poetry, caches the virtual environment, and installs dependencies.

## Planned Enhancements

- **Microservices Architecture**: Separate model building and prediction services for a more modular and scalable architecture.
- **Advanced Neural Network Development**: Enhance the neural network for improved prediction accuracy.
- **Deployment Ready**: Make the application deployment-ready with Docker and Kubernetes.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
