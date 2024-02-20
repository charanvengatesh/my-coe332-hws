# ISS Trajectory Tracker

## Overview

This project aims to provide a tool for querying and visualizing the International Space Station (ISS) trajectory data over a 15-day period. It is designed to ingest ISS state vector data, calculate and display various metrics such as average speed, and find the position and velocity of the ISS closest to the current time. This tool is important for educational purposes, allowing users to understand and interact with space data in a meaningful way.

## Folder Contents / Project Objective

- Dockerfile: Configuration for containerizing the application.
- iss_tracker.py: Python script to fetch, process, and display ISS trajectory data.
- test_iss_tracker.py: Unit tests for various components of the iss_tracker.py script.
- README.md: Documentation explaining the project, its setup, and usage.

The project simplifies the process of accessing and analyzing ISS trajectory data, making space data more accessible to the public.

## Accessing the Data Set
The ISS trajectory data is publicly available from the NASA public data portal. This data includes state vectors (position and velocity in Cartesian coordinates) of the ISS over a 15-day period, updated regularly. The data is provided in XML format, which our script processes to extract relevant information.

## Building the Container
To containerize the ISS Tracker application, ensure Docker is installed on your system, then run the following command in the project's root directory:

```
docker build -t iss-tracker .
```

This command builds a Docker image named iss-tracker based on the instructions in the Dockerfile.

## Running the Containerized Application
Once the image is built, you can run the application using Docker:

```
docker run iss-tracker
```

This command starts a container instance of iss-tracker, executing the iss_tracker.py script.

## Running Unit Tests
To run unit tests within the container, you can override the default command with the pytest command. Assuming your tests are in test_iss_tracker.py, run:

```
docker run iss-tracker pytest test_iss_tracker.py
```

## Expected Output and Interpretation
Upon running, the script outputs:

The range of data (start and end timestamps of the 15-day period).
The position and velocity of the ISS closest to the current time.
The average speed of the ISS over the data set.
The instantaneous speed of the ISS closest to "now".
