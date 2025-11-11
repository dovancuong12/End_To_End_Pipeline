import pandas as pd
from sqlalchemy import create_engine
from abc import ABC, abstractmethod
import logging

class BaseIngestor(ABC):
    """
    Abstract base class for all data ingestors.
    Provides common functionality and interface for data ingestion.
    """
    
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
        # Extract source-specific configuration from the main config
        self.source_config = config.get('sources', {}).get(source_name, {})
        # Create database engine for loading data if needed
        self.engine = create_engine(config['database_connection'])
        
        # Create logger instance for this ingestor
        # Uses the class name and source name for unique identification
        self.logger = logging.getLogger(f"{self.__class__.__name__}.{source_name}")
        
        # Configure logger if it doesn't already have handlers
        if not self.logger.handlers:
            # Create console handler for logging
            handler = logging.StreamHandler()
            # Define the format for log messages
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            # Apply the formatter to the handler
            handler.setFormatter(formatter)
            # Add the handler to the logger
            self.logger.addHandler(handler)
            # Set the logging level to INFO
            self.logger.setLevel(logging.INFO)
    
    @abstractmethod
    def extract(self):
        """
        Abstract method to extract data from the source.
        Must be implemented by subclasses.
        
        Returns:
            The extracted data in an appropriate format depending on the source type.
        """
        pass