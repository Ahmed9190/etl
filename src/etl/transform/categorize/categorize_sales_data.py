import pandas as pd

from utils.data_utils import categorize_column_into_low_medium_high

# date,product,amount,quantity

def categorize_sales_date_into_weekday(data: pd.DataFrame) -> pd.DataFrame:
    """
    Categorize the 'date' column into weekday.

    Parameters:
    - data (pd.DataFrame): Input data as a Pandas DataFrame.

    Returns:
    - pd.DataFrame: Data with a new 'weekday' column.
    """
    data['weekday'] = pd.to_datetime(data['date']).dt.weekday
    return data

def categorize_sales_date_into_month(data: pd.DataFrame) -> pd.DataFrame:
    """
    Categorize the 'date' column into month.

    Parameters:
    - data (pd.DataFrame): Input data as a Pandas DataFrame.

    Returns:
    - pd.DataFrame: Data with a new 'month' column.
    """
    data['month'] = pd.to_datetime(data['date']).dt.month
    return data

def categorize_sales_date_into_quarter(data: pd.DataFrame) -> pd.DataFrame:
    """
    Categorize the 'date' column into quarter.

    Parameters:
    - data (pd.DataFrame): Input data as a Pandas DataFrame.

    Returns:
    - pd.DataFrame: Data with a new 'quarter' column.
    """
    data['quarter'] = pd.to_datetime(data['date']).dt.quarter
    return data

def categorize_sales_date_into_year(data: pd.DataFrame) -> pd.DataFrame:
    """
    Categorize the 'date' column into year.

    Parameters:
    - data (pd.DataFrame): Input data as a Pandas DataFrame.

    Returns:
    - pd.DataFrame: Data with a new 'year' column.
    """
    data['year'] = pd.to_datetime(data['date']).dt.year
    return data

def categorize_amount(data: pd.DataFrame) -> pd.DataFrame:
    """
    Categorize the 'amount' column into low, medium, and high.

    Parameters:
    - data (pd.DataFrame): Input data as a Pandas DataFrame.

    Returns:
    - pd.DataFrame: Data with a new 'amount_category' column.
    """
    data['amount_category'] = categorize_column_into_low_medium_high(data, 'amount', breakpoints=[0, 100, 500])
    return data

def categorize_quantity(data: pd.DataFrame) -> pd.DataFrame:
    """
    Categorize the 'quantity' column into low, medium, and high.

    Parameters:
    - data (pd.DataFrame): Input data as a Pandas DataFrame.

    Returns:
    - pd.DataFrame: Data with a new 'quantity_category' column.
    """
    data['quantity_category'] = categorize_column_into_low_medium_high(data, 'quantity', breakpoints=[0, 10, 50])
    return data