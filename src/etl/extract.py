import pandas as pd
import requests

def extrect_from_csv(csv_file:str)->pd.DataFrame:
  """
  Extracts data from a CSV file and returns a pandas DataFrame.

  Parameters:
  csv_file (str): The path to the CSV file.

  Returns:
  pandas.DataFrame: The extracted data as a DataFrame.
  """
  try:
    data = pd.read_csv(csv_file)
    return data
  except FileNotFoundError:
    print(f"Error: File not found - {csv_file}")
    return None
  except Exception as e:
    print(f"Error: An error occurred - {e}")
    return None

def extract_from_api(url:str)->pd.DataFrame:
  """
  Extracts data from an API and returns a pandas DataFrame.

  Parameters:
  url (str): The URL of the API.

  Returns:
  pandas.DataFrame: The extracted data as a DataFrame.
  """
  try:
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)
  except requests.exceptions.RequestException as e:
    print(f"Error: An error occurred - {e}")
    return None
  except Exception as e:
    print(f"Error: An error occurred - {e}")
    return None