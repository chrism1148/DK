import pandas as pd
import re
import csv
import os


game_date = 20180408


################################## START OF NO CHANGE POLICY ##############################

lineup_path        = ('/Users/Chris/Desktop/Statis/MLB/2018/formatted_lineups/')
projection_path    = ('/Users/Chris/Desktop/Statis/MLB/2018/formatted_projections/')


ifile_1   = os.path.join(lineup_path, 'dk_mlb_lineup_comparison_upload_%d.csv' % (game_date))
ifile_2   = os.path.join(projection_path, 'dk_mlb_projection_comparison_upload_%d.csv' % (game_date))


lineups = pd.read_csv(ifile_1)
lineups.columns = ['game_date', 'source', 'pitcher_1', 'pitcher_2', 'catcher', 'first_base', 'second_base', 'third_base', 'short_stop', 'outfield_1', 'outfield_2', 'outfield_3', 'lineup_salary']


projections = pd.read_csv(ifile_2)
projections.columns = ['game_date', 'player', 'team', 'opponent', 'postion', 'salary', 'my_proj', 'rotoql_proj', 'dfs_guru_proj', 'last_5_games_avg', 'season_avg', 'dk_points']


lineups_compare = pd.merge(lineups, projections, how='outer', on='game_date')
dk_points_dict = pd.Series(projections.dk_points.values, index=projections.player).to_dict()

 
lineup_source = lineups['source']
pitcher_1 = lineups['pitcher_1']
pitcher_1_points = pitcher_1.map(dk_points_dict)

pitcher_2 = lineups['pitcher_2']
pitcher_2_points = pitcher_2.map(dk_points_dict)

catcher = lineups['catcher']
catcher_points = catcher.map(dk_points_dict)

first_base = lineups['first_base']
first_base_points = first_base.map(dk_points_dict)

second_base = lineups['second_base']
second_base_points = second_base.map(dk_points_dict)

third_base = lineups['third_base']
third_base_points = third_base.map(dk_points_dict)

short_stop = lineups['short_stop']
short_stop_points = short_stop.map(dk_points_dict)

outfield_1 = lineups['outfield_1']
outfield_1_points = outfield_1.map(dk_points_dict)

outfield_2 = lineups['outfield_2']
outfield_2_points = outfield_2.map(dk_points_dict)

outfield_3 = lineups['outfield_3']
outfield_3_points = outfield_3.map(dk_points_dict)



lineup_results = pd.DataFrame()
lineup_results['game_date'] = lineups_compare['game_date']
lineup_results['source']  = lineup_source

lineup_results['pitcher_1'] = pitcher_1
lineup_results['pitcher_1_points'] = pitcher_1_points

lineup_results['pitcher_2'] = pitcher_2
lineup_results['pitcher_2_points'] = pitcher_2_points

lineup_results['catcher'] = catcher
lineup_results['catcher_points'] = catcher_points

lineup_results['first_base'] = first_base
lineup_results['first_base_points'] = first_base_points

lineup_results['second_base'] = second_base
lineup_results['second_base_points'] = second_base_points

lineup_results['third_base'] = third_base
lineup_results['third_base_points'] = third_base_points

lineup_results['short_stop'] = short_stop
lineup_results['short_stop_points'] = short_stop_points

lineup_results['outfield_1'] = outfield_1
lineup_results['outfield_1_points'] = outfield_1_points

lineup_results['outfield_2'] = outfield_2
lineup_results['outfield_2_points'] = outfield_2_points

lineup_results['outfield_3'] = outfield_3
lineup_results['outfield_3_points'] = outfield_3_points

lineup_results['lineup_score']  = pitcher_1_points + pitcher_2_points + catcher_points + first_base_points + second_base_points + third_base_points + short_stop_points + outfield_1_points + outfield_2_points + outfield_3_points


lineup_results.to_csv('dk_mlb_lineup_results_%d.csv' % (game_date))






