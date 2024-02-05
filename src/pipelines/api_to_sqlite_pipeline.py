from etl.extract import extract_from_api
from etl.load import load_to_sqlite
from utils.data_utils import capitalize_first_character_in_column_names
from utils.pipeline_utils import execute_pipeline


def api_to_sqlite_pipeline(api_url: str, db_uri: str, table_name: str)-> bool:
  """
  Extract, transform columns names to , and load data from an API into a SQLite database using SQLAlchemy.

  Parameters:
  - api_url (str): URL to the API endpoint.
  - db_uri (str): Database URI (e.g., 'sqlite:///example.db' for SQLite).
  - table_name (str): Name of the table to create or replace in the database.

  Returns:
  - bool: True if the pipeline runs successfully, False otherwise.
  """
  return execute_pipeline(
    extract_func=lambda: extract_from_api(api_url),
    transform_func=lambda data: capitalize_first_character_in_column_names(data),
    load_func=lambda data: load_to_sqlite(data, db_uri, table_name)
  )