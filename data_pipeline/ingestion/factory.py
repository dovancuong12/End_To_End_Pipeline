from data_pipeline.ingestion.ingestion_from_csv import CSVIngestor
from data_pipeline.ingestion.ingestion_from_yaml import YAMLIngestor
from data_pipeline.ingestion.ingestion_from_xml import XMLIngestor

class IngestorFactory:
    """Factory to dynamically create ingestor based on type."""

    registry = {
        "csv": CSVIngestor,
        "yaml": YAMLIngestor,
        "xml": XMLIngestor,
        # "sql": SQLIngestor,  # add later if needed
    }

    @classmethod
    def create(cls, source_type: str):
        if source_type not in cls.registry:
            raise ValueError(f"Unsupported source type: {source_type}")
        return cls.registry[source_type]
