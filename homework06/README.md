
# Gene Explorer API

## High-Level Description

The Gene Explorer API provides a simple yet powerful interface for fetching and managing genetic data. Leveraging Docker for containerization, this project utilizes Flask for the web framework and Redis as a caching layer to store fetched gene data. This setup enables efficient data retrieval and management, catering to both educational and research purposes.

## Main Files Overview

- `Dockerfile`: Contains instructions for building the Docker image for the Flask application, including setting up the working directory, copying the project files, installing dependencies, and specifying the command to run the app.
- `docker-compose.yaml`: Defines the services required for the application, including the Flask app and the Redis database, their configuration, ports, and volumes for persistence.
- `app.py`: The core Flask application that defines endpoints for posting, getting, and deleting gene data from Redis, as well as fetching detailed information about genes.
- `requirements.txt`: A list of Python package dependencies needed to run the Flask application.

## Building the Docker Image

To build the Docker image for the Flask application, navigate to the project directory and run:

```shell
docker build -t flask-app .
```

## Launching the Application with Docker-Compose

To start the Flask application and Redis service, use `docker-compose`:

```shell
docker-compose up -d
```

This command will start the containers in the background. To check the status of the containers, use:

```shell
docker-compose ps
```

## API Query Examples

### Store Data in Redis

```shell
curl -X POST http://localhost:3000/data
```

Expected output:

```
Data stored in Redis
```

### Retrieve Data from Redis

```shell
curl http://localhost:3000/data
```

Expected output:

```json
{
  "data": "Gene data here..."
}
```

### Delete Data from Redis

```shell
curl -X DELETE http://localhost:3000/data
```

Expected output:

```
Data deleted from Redis
```

### Fetch Genes

```shell
curl http://localhost:3000/genes
```

Expected output:

```json
[
  {
    "hgnc_id": "Gene ID",
    "gene": "Gene details..."
  }
]
```

### Fetch a Single Gene by ID

```shell
curl http://localhost:3000/genes/<gene_id>
```

Expected output for a valid gene ID:

```json
{
  "hgnc_id": "Specific gene ID",
  "gene": "Specific gene details..."
}
```

## Data Description

The gene data fetched and managed by this API is sourced from the HGNC (HUGO Gene Nomenclature Committee), which provides authoritative, standardized naming for human genes. The dataset includes gene names, identifiers (such as HGNC ID), and other relevant genetic information. This data is critical for researchers and educators in genomics, providing a foundation for genetic research and study.

Source: [HGNC](https://www.genenames.org/download/archive/)
