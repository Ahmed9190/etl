import requests
import pandas as pd

def api_to_csv_pipeline(api_url:str, csv_file:str) -> bool:
  try:
    response = requests.get(api_url)
    data = response.json()
    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)
    return True
  except Exception as e:
    print(f"Error: {e}")
    return False