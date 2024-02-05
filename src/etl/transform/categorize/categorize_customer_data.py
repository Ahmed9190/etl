import pandas as pd

def categorize_customer_name(data: pd.DataFrame)-> pd.DataFrame:
  """
  Categorize the 'name' column into common, uncommon, and rare.

  Parameters:
  - data (pd.DataFrame): Input data as a Pandas DataFrame.

  Returns:
  - pd.DataFrame: Data with a new 'name_category' column.
  """
  data['name_category'] = pd.cut(data['name'], bins=[0, 100, 500, float('inf')], labels=['common', 'uncommon', 'rare'])
  return data

def categorize_age(data: pd.DataFrame)-> pd.DataFrame:
  """
  Categorize the 'age' column into young, adult, and senior.

  Parameters:
  - data (pd.DataFrame): Input data as a Pandas DataFrame.

  Returns:
  - pd.DataFrame: Data with a new 'age_category' column.
  """
  data['age_category'] = pd.cut(data['age'], bins=[0, 30, 60, float('inf')], labels=['young', 'adult', 'senior'])
  return data