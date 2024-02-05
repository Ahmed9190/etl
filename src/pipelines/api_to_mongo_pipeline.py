from etl.extract import extract_from_api
from etl.load import load_to_mongo
from utils.data_utils import capitalize_first_character_in_column_names
from utils.pipeline_utils import execute_pipeline


def api_to_mongo_pipeline(api_url: str, db_uri: str, collection_name: str)-> bool:
  """
  Extract, transform columns names to , and load data from an API into a Mongo.

  Parameters:
  - api_url (str): URL to the API endpoint.
  - db_uri (str): Database URI (e.g., 'mongodb://localhost:27017/' for MongoDB).
  - collection_name (str): Name of the collection to create or replace in the database.

  Returns:
  - bool: True if the pipeline runs successfully, False otherwise.
  """
  return execute_pipeline(
    extract_func=lambda: extract_from_api(api_url),
    transform_func=lambda data: capitalize_first_character_in_column_names(data),
    load_func=lambda data: load_to_mongo(data, db_uri, collection_name)
  )