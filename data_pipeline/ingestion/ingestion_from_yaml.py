import pandas as pd
import yaml
from pathlib import Path
from typing import Any, Dict
from data_pipeline.ingestion.base_ingestor import BaseIngestor

class YAMLIngestor(BaseIngestor):
    """
    Ingestor for YAML data source.
    - Reads YAML data from file path in config
    - Flattens nested structures into a DataFrame
    - Returns metadata for downstream DAG processing
    """

    def extract(self) -> Dict[str, Any]:
        path = self.source_config.get("path")
        if not path:
            msg = f"'path' not specified in source configuration for {self.source_name}"
            self.logger.error(msg)
            raise ValueError(msg)

        self.logger.info(f"[{self.source_name}] Reading YAML file: {path}")

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)

            # Normalize YAML to DataFrame (handle nested structures)
            df = pd.json_normalize(data)

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

        except Exception as e:
            self.logger.exception(f"[{self.source_name}] Failed to read YAML: {e}")
            raise
