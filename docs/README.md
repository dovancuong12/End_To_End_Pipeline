# End-to-End Data Pipeline Documentation

## Overview
This repository contains a complete end-to-end data pipeline solution that handles data ingestion, processing, quality assurance, and visualization.

## Architecture
The system is composed of several key components:

### Batch Processing Pipeline
- Data extraction from MySQL
- Data validation using Great Expectations
- Data storage in MinIO (raw zone)
- Data transformation using Apache Spark
- Data loading to PostgreSQL (processed zone)

### Streaming Processing Pipeline
- Real-time data ingestion via Kafka
- Stream processing with Spark Structured Streaming
- Anomaly detection with ML models
- Real-time storage in PostgreSQL and MinIO

### Data Quality & Governance
- Automated data validation with Great Expectations
- Data lineage tracking with OpenMetadata/Atlas
- Metrics collection with Prometheus
- Monitoring and alerting with Grafana

### Access Control & Security
- User management with Keycloak
- Secret management with Vault

## SDK Usage
The pipeline includes an SDK for easy integration and management:

```bash
pip install end-to-end-pipeline-sdk
```

Configuration:
```python
from sdk.your_sdk import client

# Initialize the client
config = {
    'database': {
        'postgres': {
            'host': 'localhost',
            'port': 5432,
            # ... other config
        }
    }
    # ... other configurations
}

pipeline_client = client.PipelineClient(config)
```

## Infrastructure
The entire infrastructure can be deployed using Docker Compose:

```bash
docker-compose -f infra/docker-compose.yml up -d
```

## Development
To set up the development environment:

```bash
make dev-install
make run-airflow
```

## Project Structure
```
End-To-End-Pipeline/
├── airflow/              # Airflow DAGs and plugins
├── config/              # Configuration files
├── db/                  # Database initialization scripts
├── governance/          # Data governance configurations
├── infra/               # Infrastructure as code
├── kafka/               # Kafka consumers and producers
├── monitoring/          # Monitoring configurations
├── sdk/                 # Pipeline SDK
├── spark/               # Spark jobs (batch & streaming)
├── scripts/             # Utility scripts
└── docs/                # Documentation