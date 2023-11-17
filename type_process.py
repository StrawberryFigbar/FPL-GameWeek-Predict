import pandas as pd

data_raw_url = 'Data/time_series_data_raw.csv'
data_raw = pd.read_csv(data_raw_url)
data_raw['was_home'] = data_raw['was_home'].astype(int)
data_raw['was_home_1'] = data_raw['was_home_1'].astype(int)
data_raw['was_home_2'] = data_raw['was_home_2'].astype(int)
data_raw['was_home_3'] = data_raw['was_home_3'].astype(int)
data_raw.to_csv('time_series_data_raw.csv', index=False)
