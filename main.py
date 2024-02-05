from pipelines.api_to_csv_pipeline import api_to_csv_pipeline
from pipelines.api_to_mongo_pipeline import api_to_mongo_pipeline
from pipelines.api_to_sqlite_pipeline import api_to_sqlite_pipeline
from pipelines.csv_to_sqlite_pipeline import csv_to_sqlite_pipeline
from pipelines.csv_to_mongo_pipeline import csv_to_mongo_pipeline
from os import environ

def main():
  run_csv_to_sqlite_pipeline()
  run_api_to_sqlite_pipeline()
  run_csv_to_mongo_pipeline()
  run_api_to_mongo_pipeline()
  run_api_to_csv_pipeline()

sqilite_db_uri:str = environ.get("SQLITE_DATABASE_PATH")
api_url:str = 'https://jsonplaceholder.typicode.com/users'
mongo_db_uri:str = environ.get("MONGO_DATABASE_URI")

def run_csv_to_sqlite_pipeline():
  csv_to_sqlite_success = csv_to_sqlite_pipeline(
    csv_file='data/input/csv_data/sales_data.csv',
    db_uri=sqilite_db_uri,
    table_name='sales_table'
  )

  if csv_to_sqlite_success:
    print("CSV to SQLite pipeline ran successfully.")
  else:
    print("CSV to SQLite pipeline failed.")

def run_api_to_sqlite_pipeline():
  api_to_sqlite_success = api_to_sqlite_pipeline(
    api_url=api_url,
    db_uri=sqilite_db_uri,
    table_name='users'
  )

  if api_to_sqlite_success:
    print("API to SQLite pipeline ran successfully.")
  else:
    print("API to SQLite pipeline failed.")

def run_csv_to_mongo_pipeline():
  csv_to_mongo_success = csv_to_mongo_pipeline(
    csv_file='data/input/csv_data/sales_data.csv',
    db_uri=mongo_db_uri,
    collection_name='sales'
  )

  if csv_to_mongo_success:
    print("CSV to Mongo pipeline ran successfully.")
  else:
    print("CSV to Mongo pipeline failed.")


def run_api_to_mongo_pipeline():
  api_to_mongo_success = api_to_mongo_pipeline(
    api_url= api_url,
    db_uri=mongo_db_uri,
    collection_name='users'
  )

  if api_to_mongo_success:
    print("API to Mongo pipeline ran successfully.")
  else:
    print("API to Mongo pipeline failed.")

def run_api_to_csv_pipeline():
  api_to_csv_success = api_to_csv_pipeline(
    api_url=api_url,
    csv_file='data/output/csv/users.csv'
  )

  if api_to_csv_success:
    print("API to CSV pipeline ran successfully.")
  else:
    print("API to CSV pipeline failed.")

if __name__ == '__main__':
  main()