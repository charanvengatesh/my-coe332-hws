# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir requests xmltodict pytest

# Run iss_tracker.py when the container launches
CMD ["python", "./iss_tracker.py"]
