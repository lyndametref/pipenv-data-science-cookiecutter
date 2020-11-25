import os
import pandas as pd
from src.config import get_path


def write_cache_pickle(df: pd.DataFrame, filename: str):
    cache_path = get_path('cache_path')
    filepath = os.path.join(cache_path, filename)
    df.to_pickle(filepath)


def read_cache_pickle(filename: str) -> pd.DataFrame:
    cache_path = get_path('cache_path')
    filepath = os.path.join(cache_path, filename)
    return pd.read_pickle(filepath)
