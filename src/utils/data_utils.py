import pandas as pd

def categorize_column_into_low_medium_high(data: pd.DataFrame, column: str, breakpoints: list) -> pd.DataFrame:
    """
    Categorize a column into low, medium, and high.

    Parameters:
    - data (pd.DataFrame): Input data as a Pandas DataFrame.
    - column (str): The column to categorize.
    - breakpoints (list): The breakpoints to use for categorization.

    Returns:
    - pd.DataFrame: Data with a new categorized column.
    """
    bins = breakpoints + [float('inf')]
    data[f'{column}_category'] = pd.cut(data[column], bins=bins, labels=['low', 'medium', 'high'])
    return data

def capitalize_first_character_in_column_names(data: pd.DataFrame) -> pd.DataFrame:
    """
    Capitalize the first character in each column name.

    Parameters:
    - data (pd.DataFrame): Input data as a Pandas DataFrame.

    Returns:
    - pd.DataFrame: Data with capitalized column names.
    """
    data.columns = [col.capitalize() for col in data.columns]
    return data