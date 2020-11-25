import os
import pandas as pd
from src.config import set_log_config, get_path
from src.cache import write_cache_pickle, read_cache_pickle

logger = set_log_config(__file__)
cache_filename = 'data_cache.pkl'
df = pd.read_csv(os.path.join(get_path('data_path'), 'data.csv'))
df['day'] = pd.to_datetime(df['day'])
df['temp'] = (df.temp_min + df.temp_max) / 2

write_cache_pickle(df, cache_filename)
logger.info(str(df.shape[0]) + " rows written to " + cache_filename)

read_df = read_cache_pickle(cache_filename)
logger.info(str(read_df.shape[0]) + " rows read from " + cache_filename)
print(read_df)
