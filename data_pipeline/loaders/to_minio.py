from minio import Minio
from common.config.configs import MinIOConfigs

def get_minio_client():
    cfg = MinIOConfigs()
    return Minio(
        endpoint=cfg.endpoint,
        access_key=cfg.access_key,
        secret_key=cfg.secret_key,
        secure=cfg.secure,
    )