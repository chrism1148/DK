import pandas as pd
import re
import csv
import os


game_date = 20180417


################################## START OF NO CHANGE POLICY ##############################

#path to file directory - HOME
# lineup_path        = ('/Users/Chris/Desktop/Statis/MLB/2018/formatted_lineups/')
# projection_path    = ('/Users/Chris/Desktop/Statis/MLB/2018/formatted_projections/')

#path to file directory - WORK
my_projection_path  = ('/Users/chrismccallan/downloads/')
rotoql_path       = ('/Users/chrismccallan/downloads/')

#load date specific files from path
ifile_1   = os.path.join(my_projection_path, 'dk_mlb_my_projections_%d.csv' % (game_date))
ifile_2   = os.path.join(rotoql_path, 'dk_mlb_rotoql_%d.csv' % (game_date))

# read files to dataframe for formatting
my_projection = pd.read_csv(ifile_1)
my_projection.columns = ['Player', 'Team', 'Opponent', 'Position', 'Salary', 'MyProjection' ]

rotoql = pd.read_csv(ifile_2)
rotoql.columns = ['player_id', 'mlb_id', 'Player', 'dk_salary', 'fd_salary', 'yh_salary', 'rst_salary', 'position', 'team', 'opponent', 'dk_value', 'fd_value', 'yh_value', 'rst_value']


# merge ifile_1 and ifile_2 to create the dictionary {'player': 'point value'}
projection_merge       = pd.merge(lineups, projections, how='outer', on='Player')
# dk_points_dict        = pd.Series(projections.dk_points.values, index=projections.player).to_dict()

projection_merge.to_csv('rotoql_upload_%d' % (game_date))