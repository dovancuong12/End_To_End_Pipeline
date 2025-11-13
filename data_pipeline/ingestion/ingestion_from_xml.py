import pandas as pd
from pathlib import Path
from typing import Any, Dict
from data_pipeline.ingestion.base_ingestor import BaseIngestor

class XMLIngestor(BaseIngestor):
    """
    Ingestor for XML data source.
    - Reads XML data from file path in config
    - Converts XML tree into a structured DataFrame
    - Returns metadata for downstream DAG processing
    """

    def extract(self) -> Dict[str, Any]:
        path = self.source_config.get("path")
        if not path:
            msg = f"'path' not specified in source configuration for {self.source_name}"
            self.logger.error(msg)
            raise ValueError(msg)

        xpath = self.source_config.get("xpath", ".//*")  # default: read all nodes
        self.logger.info(f"[{self.source_name}] Reading XML file: {path} (xpath={xpath})")

        try:
            df = pd.read_xml(path, xpath=xpath)
            df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

            schema_info = {
                col: {
                    "type": str(df[col].dtype),
                    "non_null_count": int(df[col].count()),
                    "null_count": int(df[col].isnull().sum()),
                    "unique_values": int(df[col].nunique()),
                }
                for col in df.columns
            }

            tmp_path = Path("/tmp") / f"{self.source_name}.parquet"
            df.to_parquet(tmp_path, index=False)

            result = {
                "path": str(tmp_path),
                "rows": len(df),
                "columns": len(df.columns),
                "schema_info": schema_info,
            }

            self.logger.info(
                f"[{self.source_name}] Extracted {result['rows']} rows, "
                f"{result['columns']} cols -> saved to {tmp_path}"
            )

            return result

        except (FileNotFoundError, ValueError) as e:
            self.logger.exception(f"[{self.source_name}] Failed to read XML: {e}")
            raise
