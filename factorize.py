import pandas as pd


data_url = f'Data/time_series_data_raw.csv'
data = pd.read_csv(data_url)
# Create a dictionary to map team names to numbers
team_dic = {}
position_dic = {}
# Use the factorize function to map team names to unique numbers
data['team_x'], team_dic = pd.factorize(data['team_x'])
data['position'], position_dic = pd.factorize(data['position'])

# Print the updated DataFrame

team_list = pd.DataFrame(team_dic)

position_list = pd.DataFrame(position_dic)

data.to_csv(f'Data/time_series_data.csv', index=False)
team_list.to_csv(f'Data/team_list.csv', index=False)
position_list.to_csv(f'Data/position_list.csv', index=False)
