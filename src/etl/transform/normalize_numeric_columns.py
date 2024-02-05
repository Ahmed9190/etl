import pandas as pd

def normalize_numeric_columns(data: pd.DataFrame)-> pd.DataFrame:
    """
    Normalize numeric columns to a 0-1 scale in the DataFrame.

    Parameters:
    - data (pd.DataFrame): Input data as a Pandas DataFrame.

    Returns:
    - pd.DataFrame: Data with numeric columns normalized.
    """
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    data[numeric_columns] = (data[numeric_columns] - data[numeric_columns].min()) / (data[numeric_columns].max() - data[numeric_columns].min())
    return data