import pandas as pd

train_url = f'Data_Raw/cleaned_merged_seasons.csv'
train = pd.read_csv(train_url)
train = train.sort_values(['name', 'season_x', 'GW'])
train = train.reset_index()
current_game_week = ['name', 'position', 'team_x', 'opponent_team', 'was_home']
weeks_direct = ['assists_1', 'assists_2', 'assists_3',
                'goals_scored_1', 'goal_scored_2', 'goal_scored_3',
                'goals_conceded_1', 'goals_conceded_2', 'goals_conceded_3',
                'saves_1', 'saves_2', 'saves_3',
                'clean_sheets_1', 'clean_sheets_2', 'clean_sheets_3',
                'minutes_1', 'minutes_2', 'minutes_3',
                'selected_1', 'selected_2', 'selected_3',
                'transfers_in_1', 'transfers_in_2', 'transfers_in_3',
                'transfers_out_1', 'transfers_out_2', 'transfers_out_3']
weeks_fixture = ['opponent_team_1', 'opponent_team_2', 'opponent_team_3',
                 'team_a_score_1', 'team_a_score_2', 'team_a_score_3',
                 'team_h_score_1', 'team_h_score_2', 'team_h_score_3',
                 'was_home_1', 'was_home_2', 'was_home_3']
weeks_meta = ['bonus_1', 'bonus_2', 'bonus_3',
              'bps_1', 'bps_2', 'bps_3',
              'creativity_1', 'creativity_2', 'creativity_3',
              'ict_index_1', 'ict_index_2', 'ict_index_3',
              'influence_1', 'influence_2', 'influence_3',
              'threat_1', 'treat_2', 'treat_3',
              'value_1', 'value_2', 'value_3']
weeks_niche = ['own_goals_1', 'own_goals_2', 'own_goals_3',
               'penalties_missed_1', 'penalties_missed_2', 'penalties_missed_3',
               'penalties_saved_1', 'penalties_saved_2', 'penalties_saved_3',
               'yellow_cards_1', 'yellow_cards_2', 'yellow_cards_3',
               'red_cards_1', 'red_cards_2', 'red_cards_3']
target = ['total_points']
print
data_columns = (current_game_week + weeks_direct + weeks_fixture +
                weeks_meta + weeks_niche+target)
time_series_data = pd.DataFrame(columns=data_columns)

for i in range(0, 96166):
    if train['name'][i] == train['name'][i+3] and train['GW'][i] + 3 == train['GW'][i+3]:
        current_game_week_data = [train['name'][i+3], train['position'][i+3], train['team_x']
                                  [i+3], train['opponent_team'][i+3], train['was_home'][i+3]]
        weeks_direct_data = [train['assists'][i],
                             train['assists'][i+1], train['assists'][i +
                                                                     2], train['goals_scored'][i],
                             train['goals_scored'][i+1], train['goals_scored'][i +
                                                                               2], train['goals_conceded'][i],
                             train['goals_conceded'][i +
                                                     1], train['goals_conceded'][i+2], train['saves'][i],
                             train['saves'][i+1], train['saves'][i +
                                                                 2], train['clean_sheets'][i],
                             train['clean_sheets'][i +
                                                   1], train['clean_sheets'][i+2], train['minutes'][i],
                             train['minutes'][i+1], train['minutes'][i +
                                                                     2], train['selected'][i],
                             train['selected'][i+1], train['selected'][i +
                                                                       2], train['transfers_in'][i],
                             train['transfers_in'][i+1], train['transfers_in'][i +
                                                                               2], train['transfers_out'][i],
                             train['transfers_out'][i+1], train['transfers_out'][i+2]]
        weeks_fixture_data = [train['opponent_team'][i],
                              train['opponent_team'][i+1], train['opponent_team'][i +
                                                                                  2], train['team_a_score'][i],
                              train['team_a_score'][i+1], train['team_a_score'][i +
                                                                                2], train['team_h_score'][i],
                              train['team_h_score'][i+1], train['team_h_score'][i +
                                                                                2], train['was_home'][i],
                              train['was_home'][i+1], train['was_home'][i +
                                                                        2]]
        weeks_meta_data = [train['bonus'][i],
                           train['bonus'][i+1], train['bonus'][i +
                                                               2], train['bps'][i],
                           train['bps'][i+1], train['bps'][i +
                                                           2], train['creativity'][i],
                           train['creativity'][i+1], train['creativity'][i +
                                                                         2], train['ict_index'][i],
                           train['ict_index'][i+1], train['ict_index'][i +
                                                                       2], train['influence'][i],
                           train['influence'][i+1], train['influence'][i +
                                                                       2], train['threat'][i],
                           train['threat'][i+1], train['threat'][i +
                                                                 2], train['value'][i],
                           train['value'][i+1], train['value'][i+2]]
        weeks_niche_data = [train['own_goals'][i],
                            train['own_goals'][i+1], train['own_goals'][i +
                                                                        2], train['penalties_missed'][i],
                            train['penalties_missed'][i+1], train['penalties_missed'][i +
                                                                                      2], train['penalties_saved'][i],
                            train['penalties_saved'][i+1], train['penalties_saved'][i +
                                                                                    2], train['yellow_cards'][i],
                            train['yellow_cards'][i+1], train['yellow_cards'][i +
                                                                              2], train['red_cards'][i],
                            train['red_cards'][i+1], train['red_cards'][i+2]]
        target = [train['total_points'][i+3]]
        timeseries_data_line = (current_game_week_data + weeks_direct_data +
                                weeks_fixture_data + weeks_meta_data + weeks_niche_data+target)
        time_series_data.loc[len(time_series_data.index)
                             ] = timeseries_data_line
print(time_series_data.head())
time_series_data.to_csv(f'Data/time_series_data_raw.csv', index=False)
