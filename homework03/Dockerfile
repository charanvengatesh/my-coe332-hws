# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir pytest

COPY . .

CMD ["python", "./ml_data_analysis.py", "/data/meteorite_landings.csv"]

