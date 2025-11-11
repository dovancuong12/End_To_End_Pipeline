# CSV data ingestion module
import pandas as pd
from pathlib import Path
from typing import Any, Dict
from data_pipeline.ingestion.base_ingestor import BaseIngestor

class CSVIngestor(BaseIngestor):
    """
    Ingestor for CSV data source.
    - Reads data from CSV file path in config
    - Normalizes column names
    - Returns metadata for DAG processing
    """

    def extract(self) -> Dict[str, Any]:
        """
        Extract data from CSV source and return metadata.
        
        Returns:
            dict: A dictionary containing:
                - path (str): Path to temporary parquet file
                - rows (int): Number of rows in the CSV file
                - columns (int): Number of columns in the CSV file
                - schema_info (dict): Column info (dtype, nulls, uniques)
        """
        path = self.source_config.get("path")
        if not path:
            msg = f"'path' not specified in source configuration for {self.source_name}"
            self.logger.error(msg)
            raise ValueError(msg)

        encoding = self.source_config.get("encoding", "utf-8")
        delimiter = self.source_config.get("delimiter", ",")

        self.logger.info(f"[{self.source_name}] Reading CSV file: {path}")

        try:
            df = pd.read_csv(path, encoding=encoding, delimiter=delimiter)
            df.columns = [c.strip().lower() for c in df.columns]

            schema_info = {
                col: {
                    "type": str(df[col].dtype),
                    "non_null_count": int(df[col].count()),
                    "null_count": int(df[col].isnull().sum()),
                    "unique_values": int(df[col].nunique())
                }
                for col in df.columns
            }

            # Save temporary file for downstream DAGs
            tmp_path = Path("/tmp") / f"{self.source_name}.parquet"
            df.to_parquet(tmp_path, index=False)

            result = {
                "path": str(tmp_path),
                "rows": len(df),
                "columns": len(df.columns),
                "schema_info": schema_info
            }

            self.logger.info(
                f"[{self.source_name}] Extracted {result['rows']} rows, "
                f"{result['columns']} cols -> saved to {tmp_path}"
            )

            return result

        except (FileNotFoundError, pd.errors.ParserError) as e:
            self.logger.exception(f"[{self.source_name}] Failed to read CSV: {e}")
            raise
