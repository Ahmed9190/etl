import pandas as pd
import pymongo
from sqlalchemy import create_engine

def load_to_sqlite(data: pd.DataFrame, db_uri: str, table_name: str)-> bool:
  """
  Load data into a SQLite database using SQLAlchemy.

  Parameters:
  - data (pd.DataFrame): Transformed data as a Pandas DataFrame.
  - db_uri (str): Database URI (e.g., 'sqlite:///example.db' for SQLite).
  - table_name (str): Name of the table to create or replace in the database.

  Returns:
  - bool: True if loading is successful, False otherwise.
  """
  try:
    engine = create_engine(db_uri)
    data.to_sql(table_name, engine, index=False, if_exists='replace')
    print(f"Data loaded to {db_uri} table {table_name}.")
    return True
  except Exception as e:
    print(f"Error loading data to {db_uri} table {table_name}: {e}")
    return False

def load_to_mongo(data: pd.DataFrame, db_uri: str, collection_name: str)-> bool:
  """
  Load data into a Mongo database using PyMongo.

  Parameters:
  - data (pd.DataFrame): Transformed data as a Pandas DataFrame.
  - db_uri (str): Database URI (e.g., 'mongodb://localhost:27017/' for MongoDB).
  - collection_name (str): Name of the collection to create or replace in the database.

  Returns:
  - bool: True if loading is successful, False otherwise.
  """
  try:
    client = pymongo.MongoClient(db_uri)
    db = client.get_default_database()
    db[collection_name].drop()
    db[collection_name].insert_many(data.to_dict(orient='records'))
    print(f"Data loaded to {db_uri} collection {collection_name}.")
    return True
  except Exception as e:
    print(f"Error loading data to {db_uri} collection {collection_name}: {e}")
    return False