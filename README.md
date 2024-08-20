# FastAPI Boilerplate

This is a sample API built with FastAPI that can be deployed and run locally with Docker. It uses Poetry for dependency management and is intended to be used as a starting point for projects.

## Development using DevContainer

This project is set up to use a DevContainer for Python development. To use the DevContainer, you will need to have Docker and Visual Studio Code installed. When opening the DevContainer, Poetry will be installed and the dependencies will be installed. If dependencies are added, you can run `poetry install` in the terminal to install them.

Once setup is complete switch to the Poetry virtual environment by either using the Visual Studio Code IDE, or by running `poetry shell` in the terminal.

## Development without DevContainer

If you are not using the DevContainer, you can install the dependencies using Poetry, by running `poetry install` in the root directory of the project. Then, activate the virtual environment as above.

## Docker Build

To build the container image using Docker, run the following command in the root directory of the project:

`docker build -t sample-api:1.0 .`

## Run Locally with Docker

To run locally with Docker:

`docker run -d -i -p 8000:8000  sample-api:1.0`

## Run Locally with Uvicorn

To run locally with Uvicorn:

`uvicorn src.main:app --host "0.0.0.0" --port "8000"`
