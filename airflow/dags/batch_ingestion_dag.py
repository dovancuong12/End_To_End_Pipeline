from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import task
from pathlib import Path
import yaml
import logging

# Import ingestion modules
from common.logger.logger import setup_logging
from data_pipeline.ingestion.factory import IngestorFactory
from common.storage.minio_client import get_minio_client

# Configure logging once globally for DAG
setup_logging()

# Path to configuration
CONFIG_PATH = Path("/opt/airflow/dags/ingestion/configs/ingestion_config.yaml")

# Default arguments for DAG
default_args = {
    "owner": "data_engineer",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="batch_ingestion_dag",
    default_args=default_args,
    start_date=datetime(2025, 11, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["ingestion", "data_pipeline"],
    description="Batch ingestion pipeline for CSV, YAML, XML sources",
) as dag:

    # --- DAG tasks ---
    # --------------------
    # 1. LOAD CONFIG
    # --------------------
    @task()
    def load_config() -> dict:
        """Load the YAML configuration file."""
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        logging.info(f"✅ Loaded config with {len(config['sources'])} sources")
        return config

    # --------------------
    # 2. RUN INGESTION
    # --------------------
    @task()
    def run_ingestion(config: dict, source_name: str):
        """Run ingestion for one source based on type."""
        source_cfg = config["sources"][source_name]
        source_type = source_cfg["type"]

        IngestorClass = IngestorFactory.create(source_type)
        ingestor = IngestorClass(config, source_name)
        result = ingestor.extract()

        logging.info(
            f"✅ [{source_name}] Completed ingestion: {result['rows']} rows, "
            f"saved to {result['path']}"
        )

        # (Optional) upload to MinIO or S3 here
        # upload_to_minio_task(result["path"], f"raw/{source_name}.parquet")

        return result

    # --- DAG execution graph ---
    # --------------------
    # 3. UPLOAD TO MINIO
    # --------------------
    config = load_config()
    minio_client = get_minio_client()
    @task()
    def upload_to_minio(result: dict, bucket: str = "raw"):
        file_path = result["path"]
        source_name = Path(file_path).stem
        today = datetime.utcnow()

        object_key = (
            f"{source_name}/{today.year}/{today.month:02d}/{today.day:02d}/"
            f"{source_name}.parquet"
        )

        client = minio_client

        if not client.bucket_exists(bucket):
            client.make_bucket(bucket)

        client.fput_object(bucket, object_key, file_path)

        logging.info(f"📤 Uploaded to MinIO: s3://{bucket}/{object_key}")

        return {
            "bucket": bucket,
            "key": object_key,
            "local_path": file_path,
        }

    # Dynamically create ingestion tasks for each source in config
    from airflow.models.baseoperator import chain
    ingestion_tasks = []
    for src_name in yaml.safe_load(open(CONFIG_PATH))["sources"].keys():
        task = run_ingestion.override(task_id=f"ingest_{src_name}")(config, src_name)
        ingestion_tasks.append(task)

    # Define linear execution or parallel
    chain(config, *ingestion_tasks)

    # --------------------
    # BUILD DAG GRAPH
    # --------------------
    config = load_config()
    config_data = yaml.safe_load(open(CONFIG_PATH, "r"))

    for src_name in config_data["sources"].keys():
        ingest = run_ingestion.override(task_id=f"ingest_{src_name}")(config, src_name)
        upload = upload_to_minio.override(task_id=f"upload_{src_name}")(ingest)

        # You can optionally chain load_config >> ingest >> upload
        config >> ingest >> upload
