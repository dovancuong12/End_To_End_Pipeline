import pandas as pd
from sqlalchemy import create_engine
from abc import ABC, abstractmethod

class BaseIngestor(ABC):
    def __init__(self, config: dict, source_name: str):
        self.config = config
        self.source_name = source_name
        self.engine = create_engine(self.config['database_connection'])
    
    @abstractmethod
    def extract(self) -> pd.DataFrame:
        "read data from source"
        pass

    def load_to_db(self, df: pd.DataFrame) -> None:
        "load data to database"
        pass