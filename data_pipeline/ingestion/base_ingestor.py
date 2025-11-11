# data_pipeline/ingestion/base_ingestor.py
from abc import ABC, abstractmethod
from common.logger.logger import get_logger

class BaseIngestor(ABC):
    """Abstract base class for all data ingestors."""

    def __init__(self, config: dict, source_name: str):
        """
        Initialize the BaseIngestor with configuration and source name.
        
        Args:
            config (dict): Configuration dictionary containing database connection and source settings
            source_name (str): Name of the data source
        """
        # Store the full configuration
        self.config = config
        # Store the source name for identification and logging
        self.source_name = source_name
        self.source_config = config.get("sources", {}).get(source_name, {})

        # ✅ chỉ lấy instance logger, không setup handler/formatter
        self.logger = get_logger(f"{self.__class__.__name__}.{source_name}")

    @abstractmethod
    def extract(self):
        """Subclasses implement this method to extract data."""
        pass
