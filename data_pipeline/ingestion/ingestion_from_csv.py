# CSV data ingestion module
import pandas as pd
from data_pipeline.ingestion.base_ingestor import BaseIngestor

class CSVIngestor(BaseIngestor):
    """
    Ingestor for CSV data source.
    - Reads data from CSV file path in config
    - Normalizes column names
    - Returns metadata and DataFrame
    """

    def extract(self):
        """
        Extract data from CSV source and return metadata about the data.
        
        Returns:
            dict: A dictionary containing:
                - path: Path of the source CSV file
                - rows: Number of rows in the CSV file
                - columns: Number of columns in the CSV file
                - schema_info: Dictionary with column information
                - dataframe: The actual DataFrame containing the data
        """
        # Get configuration parameters
        path = self.source_config.get("path")
        encoding = self.source_config.get("encoding", "utf-8")
        delimiter = self.source_config.get("delimiter", ",")
        
        # Log the start of the reading process
        self.logger.info(f"📥 [{self.source_name}] Reading CSV file: {path}")
        
        try:
            # Read CSV file with specified encoding and delimiter
            df = pd.read_csv(path, encoding=encoding, delimiter=delimiter)
            
            # Normalize column names by stripping whitespace and converting to lowercase
            df.columns = [c.strip().lower() for c in df.columns]
            
            # Create schema information for each column
            # This includes data type, non-null count, null count, and unique values count
            schema_info = {}
            for col in df.columns:
                schema_info[col] = {
                    'type': str(df[col].dtype),  # Data type of the column
                    'non_null_count': int(df[col].count()),  # Number of non-null values
                    'null_count': int(df[col].isnull().sum()),  # Number of null values
                    'unique_values': int(df[col].nunique())  # Number of unique values
                }
            
            # Prepare the result dictionary with all required information
            result = {
                'path': path,  # Source file path
                'rows': len(df),  # Number of rows
                'columns': len(df.columns),  # Number of columns
                'schema_info': schema_info,  # Schema information
                'dataframe': df  # The actual DataFrame for further processing
            }
            
            # Log successful extraction with row and column counts
            self.logger.info(
                f"✅ [{self.source_name}] Extracted {result['rows']} rows, {result['columns']} columns from {path}"
            )
            
            # Return the result dictionary
            return result
        
        except Exception as e:
            # Log the exception with traceback and re-raise
            self.logger.exception(f"❌ [{self.source_name}] Failed to read CSV: {e}")
            raise
