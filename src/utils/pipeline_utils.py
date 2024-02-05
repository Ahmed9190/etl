import pandas as pd
from typing import Callable

def execute_pipeline(
  extract_func: Callable[[], pd.DataFrame],
  load_func: Callable[[pd.DataFrame], None],
  transform_func: Callable[[pd.DataFrame], pd.DataFrame] = lambda df: df,
) -> bool:
  """
  Execute a pipeline of extract, transform, and load functions.

  Parameters:
  - extract_func (Callable[[], pd.DataFrame]): Function to extract data from a source.
  - transform_func (Callable[[pd.DataFrame], pd.DataFrame]): Function to transform the extracted data.
  - load_func (Callable[[pd.DataFrame], None]): Function to load the transformed data into a destination.

  Returns:
  - bool: True if the pipeline runs successfully, False otherwise.
  """
  try:
    data = extract_func()
    transformed_data = transform_func(data)
    load_func(transformed_data)
    return True
  except Exception as e:
    print(f"Error running the pipeline: {e}")
    return False