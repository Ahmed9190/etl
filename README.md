# ETL Project

This project is a comprehensive Extract, Transform, Load (ETL) pipeline implemented in Python using Pandas for data manipulation and Docker for containerized deployment. The ETL process involves handling various data sources, employing transformation functions, and loading data into different database destinations.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Common Steps](#common-steps)
  - [Method 1: Without Docker](#method-1-without-docker)
  - [Method 2: With Docker](#method-2-with-docker)
  - [Method 3: With Docker Compose](#method-3-with-docker-compose)
- [Usage](#usage)
- [Customization](#customization)

## Features

- **Data Sources Handling**: The project supports multiple data sources, including:

  - **CSV Files**: Extraction and transformation functions for processing data from CSV files (`customer_data.csv` and `sales_data.csv`).
  - **API Calls**: Pipelines are implemented to extract data from APIs, enabling dynamic data retrieval and integration.

- **Transformation Functions**: The transformation stage incorporates various functions to clean, normalize, and categorize data:

  - **Handling Missing Values**: Functions to address missing values in the data.
  - **Normalizing Numeric Columns**: Functions for standardizing numeric columns in the dataset.
  - **Categorizing Data**: Specialized functions for categorizing both customer and sales data.

- **Database Destinations**:
  - **SQLite**: Implementation of pipelines to transform and load data into an SQLite database (`etl_database.db`).
  - **MongoDB**: Pipelines for transforming and loading data into MongoDB, facilitating NoSQL storage.

## Prerequisites

- [Python](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started) (optional, required for using Docker)
- [Docker Compose](https://docs.docker.com/compose/install/) (optional, required for using Docker Compose)

## Installation

### Common Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/ahmed9190/etl.git
   cd etl
   ```

2. Rename the `.env.example` file to `.env` and update the environment variables with your own values:

   ```bash
   mv .env.example .env
   ```

### Method 1: Without Docker

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the ETL pipeline:

   ```bash
    python src/main.py
   ```

### Method 2: With Docker

3. Build the Docker image:

   ```bash
   docker build -t etl .
   ```

4. Run the ETL pipeline:

   ```bash
    docker run etl
   ```

### Method 3: With Docker Compose

3. Run the ETL pipeline:

   ```bash
   docker compose up
   ```

## Usage

Run the ETL pipeline:

```bash
docker-compose up
```

## Customization

- Adjust the ETL pipeline functions in `src/pipelines/` for specific transformations.
- Update the `Dockerfile` and `docker-compose.yml` based on your project needs.
- Modify environment variables in the `.env` file for sensitive information.
