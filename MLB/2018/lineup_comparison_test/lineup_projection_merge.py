import pandas as pd
import csv
import re




lineups = pd.read_csv('dk_mlb_lineup_comparision_upload_20180408.csv')
lineups.columns = ['game_date', 'source', 'pitcher_1', 'pitcher_2', 'catcher', 'first_base', 'second_base', 'third_base', 'short_stop', 'outfield_1', 'outfield_2', 'outfield_3', 'lineup_salary']

projections = pd.read_csv('4-8.csv')
projections.columns = ['game_date', 'player', 'team', 'opponent', 'postion', 'salary', 'my_proj', 'rotoql_proj', 'dfs_guru_proj', 'last_5_games_avg', 'season_avg', 'dk_points']
lineups_compare = pd.merge(lineups, projections, how='outer', on='game_date')

dk_points_dict = pd.Series(projections.dk_points.values, index=projections.player).to_dict()

pitcher_1 = lineups['pitcher_1']
pitcher_1_points = pitcher_1.map(dk_points_dict)
# _dict.values()]


lineups_compare_out = pd.DataFrame()

lineups_compare_out['pitcher_1'] = pitcher_1
lineups_compare_out['pitcher_1_points'] = pitcher_1_points



# points_dict = {lineups_compare['player']:lineups_compare['dk_points']}

# lineup_compare['pitcher_1_points'] = lineup_compare.loc[lineup_compare['pitcher_1'] == lineup_compare['player'], lineup_compare['dk_points']]

# print(dk_points_dict)



lineups_compare_out.to_csv('lineups_test.csv')