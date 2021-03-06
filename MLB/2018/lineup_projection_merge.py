import pandas as pd
import re
import csv
import os


game_date = 20180620


################################## START OF NO CHANGE POLICY ##############################

#path to file directory - HOME
# lineup_path        = ('/Users/chris/downloads/')
# projection_path    = ('/Users/chris/downloads/')

#path to file directory - WORK
lineup_path        = ('/Users/chrismccallan/downloads/')
projection_path    = ('/Users/chrismccallan/downloads/')

#load date specific files from path
ifile_1   = os.path.join(lineup_path, 'dk_mlb_lineup_comparison_upload_%d.csv' % (game_date))
ifile_2   = os.path.join(projection_path, 'dk_mlb_projection_comparison_upload_%d.csv' % (game_date))

# read files to dataframe for formatting
lineups = pd.read_csv(ifile_1)
lineups.columns = ['game_date', 'source', 'rank', 'pitcher_1', 'pitcher_2', 'catcher', 'first_base', 'second_base', 'third_base', 'short_stop', 'outfield_1', 'outfield_2', 'outfield_3', 'lineup_salary']

projections = pd.read_csv(ifile_2, header=None, encoding='ISO-8859-1')
projections.columns = ['game_date', 'player', 'team', 'opponent', 'postion', 'salary', 'my_proj', 'rotoql_proj', 'dfs_guru_proj', 'last_5_games_avg', 'season_avg', 'dk_points', 'bp_proj']


# merge ifile_1 and ifile_2 to create the dictionary {'player': 'point value'}
lineups_compare       = pd.merge(lineups, projections, how='outer', on='game_date')
dk_points_dict        = pd.Series(projections.dk_points.values, index=projections.player).to_dict()
rotoql_proj_dict      = pd.Series(projections.rotoql_proj.values, index=projections.player).to_dict()
dfs_guru_proj_dict    = pd.Series(projections.dfs_guru_proj.values, index=projections.player).to_dict()
bp_proj_dict          = pd.Series(projections.bp_proj.values, index=projections.player).to_dict()
last_5_games_avg_dict = pd.Series(projections.last_5_games_avg.values, index=projections.player).to_dict()
season_avg_dict       = pd.Series(projections.season_avg.values, index=projections.player).to_dict()
salary_dict           = pd.Series(projections.salary.values, index=projections.player).to_dict()

#map players in specific lineup postions to the specific {'player': 'point value'} dictionary
lineup_source = lineups['source']
lineup_rank = lineups['rank']
pitcher_1 = lineups['pitcher_1']
pitcher_1_salary = pitcher_1.map(salary_dict)
pitcher_1_points = pitcher_1.map(dk_points_dict)
pitcher_1_rotoql = pitcher_1.map(rotoql_proj_dict)
pitcher_1_dfs_guru = pitcher_1.map(dfs_guru_proj_dict)
pitcher_1_bp     = pitcher_1.map(bp_proj_dict)
pitcher_1_last_5 = pitcher_1.map(last_5_games_avg_dict)
pitcher_1_season = pitcher_1.map(season_avg_dict)


pitcher_2 = lineups['pitcher_2']
pitcher_2_salary = pitcher_2.map(salary_dict)
pitcher_2_points = pitcher_2.map(dk_points_dict)
pitcher_2_rotoql = pitcher_2.map(rotoql_proj_dict)
pitcher_2_dfs_guru = pitcher_2.map(dfs_guru_proj_dict)
pitcher_2_bp     = pitcher_2.map(bp_proj_dict)
pitcher_2_last_5 = pitcher_2.map(last_5_games_avg_dict)
pitcher_2_season = pitcher_2.map(season_avg_dict)


catcher = lineups['catcher']
catcher_salary = catcher.map(salary_dict)
catcher_points = catcher.map(dk_points_dict)
catcher_rotoql = catcher.map(rotoql_proj_dict)
catcher_dfs_guru = catcher.map(dfs_guru_proj_dict)
catcher_bp     = catcher.map(bp_proj_dict)
catcher_last_5 = catcher.map(last_5_games_avg_dict)
catcher_season = catcher.map(season_avg_dict)


first_base = lineups['first_base']
first_base_salary = first_base.map(salary_dict)
first_base_points = first_base.map(dk_points_dict)
first_base_rotoql = first_base.map(rotoql_proj_dict)
first_base_dfs_guru = first_base.map(dfs_guru_proj_dict)
first_base_bp     = first_base.map(bp_proj_dict)
first_base_last_5 = first_base.map(last_5_games_avg_dict)
first_base_season = first_base.map(season_avg_dict)


second_base = lineups['second_base']
second_base_salary = second_base.map(salary_dict)
second_base_points = second_base.map(dk_points_dict)
second_base_rotoql = second_base.map(rotoql_proj_dict)
second_base_dfs_guru = second_base.map(dfs_guru_proj_dict)
second_base_bp     = second_base.map(bp_proj_dict)
second_base_last_5 = second_base.map(last_5_games_avg_dict)
second_base_season = second_base.map(season_avg_dict)


third_base = lineups['third_base']
third_base_salary = third_base.map(salary_dict)
third_base_points = third_base.map(dk_points_dict)
third_base_rotoql = third_base.map(rotoql_proj_dict)
third_base_dfs_guru = third_base.map(dfs_guru_proj_dict)
third_base_bp     = third_base.map(bp_proj_dict)
third_base_last_5 = third_base.map(last_5_games_avg_dict)
third_base_season = third_base.map(season_avg_dict)


short_stop = lineups['short_stop']
short_stop_salary = short_stop.map(salary_dict)
short_stop_points = short_stop.map(dk_points_dict)
short_stop_rotoql = short_stop.map(rotoql_proj_dict)
short_stop_dfs_guru = short_stop.map(dfs_guru_proj_dict)
short_stop_bp     = short_stop.map(bp_proj_dict)
short_stop_last_5 = short_stop.map(last_5_games_avg_dict)
short_stop_season = short_stop.map(season_avg_dict)


outfield_1 = lineups['outfield_1']
outfield_1_salary = outfield_1.map(salary_dict)
outfield_1_points = outfield_1.map(dk_points_dict)
outfield_1_rotoql = outfield_1.map(rotoql_proj_dict)
outfield_1_dfs_guru = outfield_1.map(dfs_guru_proj_dict)
outfield_1_bp     = outfield_1.map(bp_proj_dict)
outfield_1_last_5 = outfield_1.map(last_5_games_avg_dict)
outfield_1_season = outfield_1.map(season_avg_dict)


outfield_2 = lineups['outfield_2']
outfield_2_salary = outfield_2.map(salary_dict)
outfield_2_points = outfield_2.map(dk_points_dict)
outfield_2_rotoql = outfield_2.map(rotoql_proj_dict)
outfield_2_dfs_guru = outfield_2.map(dfs_guru_proj_dict)
outfield_2_bp     = outfield_2.map(bp_proj_dict)
outfield_2_last_5 = outfield_2.map(last_5_games_avg_dict)
outfield_2_season = outfield_2.map(season_avg_dict)


outfield_3 = lineups['outfield_3']
outfield_3_salary = outfield_3.map(salary_dict)
outfield_3_points = outfield_3.map(dk_points_dict)
outfield_3_rotoql = outfield_3.map(rotoql_proj_dict)
outfield_3_dfs_guru = outfield_3.map(dfs_guru_proj_dict)
outfield_3_bp     = outfield_3.map(bp_proj_dict)
outfield_3_last_5 = outfield_3.map(last_5_games_avg_dict)
outfield_3_season = outfield_3.map(season_avg_dict)


lineup_results = pd.DataFrame()
lineup_results['game_date'] = lineups['game_date']
lineup_results['source']  = lineup_source
lineup_results['rank']  = lineup_rank

lineup_results['pitcher_1'] = pitcher_1
lineup_results['pitcher_1_salary'] = pitcher_1_salary
lineup_results['pitcher_1_points'] = pitcher_1_points
lineup_results['pitcher_1_rotoql'] = pitcher_1_rotoql
lineup_results['pitcher_1_dfs_guru'] = pitcher_1_dfs_guru
lineup_results['pitcher_1_last_5'] = pitcher_1_last_5
lineup_results['pitcher_1_season'] = pitcher_1_season


lineup_results['pitcher_2'] = pitcher_2
lineup_results['pitcher_2_salary'] = pitcher_2_salary
lineup_results['pitcher_2_points'] = pitcher_2_points
lineup_results['pitcher_2_rotoql'] = pitcher_2_rotoql
lineup_results['pitcher_2_dfs_guru'] = pitcher_2_dfs_guru
lineup_results['pitcher_2_last_5'] = pitcher_2_last_5
lineup_results['pitcher_2_season'] = pitcher_2_season


lineup_results['catcher'] = catcher
lineup_results['catcher_salary'] = catcher_salary
lineup_results['catcher_points'] = catcher_points
lineup_results['catcher_rotoql'] = catcher_rotoql
lineup_results['catcher_dfs_guru'] = catcher_dfs_guru
lineup_results['catcher_last_5'] = catcher_last_5
lineup_results['catcher_season'] = catcher_season


lineup_results['first_base'] = first_base
lineup_results['first_base_salary'] = first_base_salary
lineup_results['first_base_points'] = first_base_points
lineup_results['first_base_rotoql'] = first_base_rotoql
lineup_results['first_base_dfs_guru'] = first_base_dfs_guru
lineup_results['first_base_last_5'] = first_base_last_5
lineup_results['first_base_season'] = first_base_season


lineup_results['second_base'] = second_base
lineup_results['second_base_salary'] = second_base_salary
lineup_results['second_base_points'] = second_base_points
lineup_results['second_base_rotoql'] = second_base_rotoql
lineup_results['second_base_dfs_guru'] = second_base_dfs_guru
lineup_results['second_base_last_5'] = second_base_last_5
lineup_results['second_base_season'] = second_base_season


lineup_results['third_base'] = third_base
lineup_results['third_base_salary'] = third_base_salary
lineup_results['third_base_points'] = third_base_points
lineup_results['third_base_rotoql'] = third_base_rotoql
lineup_results['third_base_dfs_guru'] = third_base_dfs_guru
lineup_results['third_base_last_5'] = third_base_last_5
lineup_results['third_base_season'] = third_base_season


lineup_results['short_stop'] = short_stop
lineup_results['short_stop_salary'] = short_stop_salary
lineup_results['short_stop_points'] = short_stop_points
lineup_results['short_stop_rotoql'] = short_stop_rotoql
lineup_results['short_stop_dfs_guru'] = short_stop_dfs_guru
lineup_results['short_stop_last_5'] = short_stop_last_5
lineup_results['short_stop_season'] = short_stop_season


lineup_results['outfield_1'] = outfield_1
lineup_results['outfield_1_salary'] = outfield_1_salary
lineup_results['outfield_1_points'] = outfield_1_points
lineup_results['outfield_1_rotoql'] = outfield_1_rotoql
lineup_results['outfield_1_dfs_guru'] = outfield_1_dfs_guru
lineup_results['outfield_1_last_5'] = outfield_1_last_5
lineup_results['outfield_1_season'] = outfield_1_season


lineup_results['outfield_2'] = outfield_2
lineup_results['outfield_2_salary'] = outfield_2_salary
lineup_results['outfield_2_points'] = outfield_2_points
lineup_results['outfield_2_rotoql'] = outfield_2_rotoql
lineup_results['outfield_2_dfs_guru'] = outfield_2_dfs_guru
lineup_results['outfield_2_last_5'] = outfield_2_last_5
lineup_results['outfield_2_season'] = outfield_2_season


lineup_results['outfield_3'] = outfield_3
lineup_results['outfield_3_salary'] = outfield_3_salary
lineup_results['outfield_3_points'] = outfield_3_points
lineup_results['outfield_3_rotoql'] = outfield_3_rotoql
lineup_results['outfield_3_dfs_guru'] = outfield_3_dfs_guru
lineup_results['outfield_3_last_5'] = outfield_3_last_5
lineup_results['outfield_3_season'] = outfield_3_season


lineup_results['lineup_salary']  = pitcher_1_salary + pitcher_2_salary + catcher_salary + first_base_salary + second_base_salary + third_base_salary + short_stop_salary + outfield_1_salary + outfield_2_salary + outfield_3_salary
lineup_results['lineup_dk_points']  = pitcher_1_points + pitcher_2_points + catcher_points + first_base_points + second_base_points + third_base_points + short_stop_points + outfield_1_points + outfield_2_points + outfield_3_points
lineup_results['lineup_rotoql_proj'] = pitcher_1_rotoql + pitcher_2_rotoql + catcher_rotoql + first_base_rotoql + second_base_rotoql + third_base_rotoql + short_stop_rotoql + outfield_1_rotoql + outfield_2_rotoql + outfield_3_rotoql
lineup_results['lineup_dfs_guru_proj'] = pitcher_1_dfs_guru + pitcher_2_dfs_guru + catcher_dfs_guru + first_base_dfs_guru + second_base_dfs_guru + third_base_dfs_guru + short_stop_dfs_guru + outfield_1_dfs_guru + outfield_2_dfs_guru + outfield_3_dfs_guru
lineup_results['lineup_last_5_proj'] = pitcher_1_last_5 + pitcher_2_last_5 + catcher_last_5 + first_base_last_5 + second_base_last_5 + third_base_last_5 + short_stop_last_5 + outfield_1_last_5 + outfield_2_last_5 + outfield_3_last_5
lineup_results['lineup_season_proj'] = pitcher_1_season + pitcher_2_season + catcher_season + first_base_season + second_base_season + third_base_season + short_stop_season + outfield_1_season + outfield_2_season + outfield_3_season
lineup_results['bp_proj'] = pitcher_1_bp + pitcher_2_bp + catcher_bp + first_base_bp + second_base_bp + third_base_bp + short_stop_bp + outfield_1_bp + outfield_2_bp + outfield_3_bp

lineup_results.to_csv('dk_mlb_lineup_results_%d.csv' % (game_date), index=False)


lineups_compare.to_csv('merge_test.csv')



