from etl.extract import extrect_from_csv
from etl.load import load_to_mongo
from utils.data_utils import capitalize_first_character_in_column_names
from utils.pipeline_utils import execute_pipeline

def csv_to_mongo_pipeline(csv_file: str, db_uri: str, collection_name: str)-> bool:
  """
  Extract, transform columns names to , and load a CSV file into a Mongo database.

  Parameters:
  - csv_file (str): File path to the input CSV file.
  - db_uri (str): Database URI (e.g., 'mongodb://localhost:27017/' for MongoDB).
  - collection_name (str): Name of the collection to create or replace in the database.

  Returns:
  - bool: True if the pipeline runs successfully, False otherwise.
  """
  return execute_pipeline(
    extract_func=lambda: extrect_from_csv(csv_file),
    transform_func=lambda data: capitalize_first_character_in_column_names(data),
    load_func=lambda data: load_to_mongo(data, db_uri, collection_name)
  )
