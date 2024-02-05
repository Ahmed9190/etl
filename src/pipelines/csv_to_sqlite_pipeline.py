from etl.extract import extrect_from_csv
from etl.load import load_to_sqlite
from utils.data_utils import capitalize_first_character_in_column_names
from utils.pipeline_utils import execute_pipeline

def csv_to_sqlite_pipeline(csv_file: str, db_uri: str, table_name: str)-> bool:
  """
  Extracts data from a CSV file, transforms it, and loads it into a SQLite database.

  Parameters:
  - csv_file (str): File path to the input CSV file.
  - db_uri (str): Database URI (e.g., 'sqlite:///example.db' for SQLite).
  - table_name (str): Name of the table to create or replace in the database.

  Returns:
  - bool: True if the pipeline runs successfully, False otherwise.
  """
  return execute_pipeline(
    extract_func=lambda: extrect_from_csv(csv_file),
    transform_func=lambda data: capitalize_first_character_in_column_names(data),
    load_func=lambda data: load_to_sqlite(data, db_uri, table_name)
  )