from pydantic import Field
from pydantic_settings import BaseSettings
from typing import Dict, List, Any, Optional

class MinIOConfigs(BaseSettings):
    endpoint: str = Field("minio:9000", alias="MINIO_ENDPOINT")
    access_key: str = Field("minioadmin", alias="MINIO_ROOT_USER")
    secret_key: str = Field("minioadmin", alias="MINIO_ROOT_PASSWORD")
    secure: bool = Field(False, alias="MINIO_SECURE")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

class PostgresConfigs(BaseSettings):
    host: str = Field("localhost", alias="POSTGRES_HOST")
    port: int = Field(5432, alias="POSTGRES_PORT")
    user: str = Field("postgres", alias="POSTGRES_USER")
    password: str = Field("postgres", alias="POSTGRES_PASSWORD")
    database: str = Field("open_asm", alias="POSTGRES_DB")

    @property
    def url(self) -> str:
        """Create connection URL"""
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"  


class AppConfigs(BaseSettings):
    host: str = Field("0.0.0.0", alias="APP_HOST")
    port: int = Field(8000, alias="APP_PORT")


class Configs(BaseSettings):
    postgres: PostgresConfigs = PostgresConfigs()
    minio: MinIOConfigs = MinIOConfigs()
    app: AppConfigs = AppConfigs()
    
    # Add missing fields used in main.py
    host: str = Field("0.0.0.0", alias="HOST")
    port: int = Field(8000, alias="PORT")
    max_workers: int = Field(10, alias="MAX_WORKERS")
    service_name: str = Field("entoend-pipeline", alias="SERVICE_NAME")
    version: str = Field("1.0.0", alias="VERSION")
    
    # Add missing fields used in domain_classifier.py
    crawl_timeout: int = Field(10, alias="CRAWL_TIMEOUT")
    crawl_max_retries: int = Field(3, alias="CRAWL_MAX_RETRIES")
    classification_confidence_threshold: float = Field(0.3, alias="CLASSIFICATION_CONFIDENCE_THRESHOLD")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

