import player_hand_lib
import player_name_lib
import position_number_lib
import player_position_lib
import team_lib
import pandas as pd
import csv
import os
import re


#HOME
# downloads = '/Users/chris/Downloads'
# formats = ('/Users/chris/Downloads')


#WORK
downloads = '/Users/chrismccallan/Downloads'
formats = ('/Users/chrismccallan/Downloads')

append_date = 20180622


ifile  = os.path.join(downloads, 'mlb_full_season_rotoguru_append_%d.csv' % (append_date))

stats = pd.read_csv(ifile)
stats.columns= ['game_date', 'rotoguru id', 'mlb id', 'player', 'starter', 'batting order', 'dk_position_number', 'dk points', 'dk salary', 'team', 'opponent', 'double header', 'team runs', 'opponent runs']


stats['player'] = stats['player'].apply(lambda x: ' '.join(x.split(',')[::-1]))
stats['player'] = stats['player'].str.strip()
stats['player'] = stats['player'].map(player_name_lib.dict)


stats['starter'] = stats['starter'].fillna(value=0)
stats['starter'] = stats['starter'].astype('int')

stats['dk_position_number'] = stats['player'].map(player_position_lib.dict)
stats['dk_position'] = stats['dk_position_number'].map(position_number_lib.dict)

stats['dk salary'] = stats['dk salary'].fillna(value=0)
stats['dk salary'] = stats['dk salary'].astype('int')

stats['team'] = stats['team'].str.lower()
stats['team'] = stats['team'].map(team_lib.dict)


stats['home-away'] = stats['opponent'].str.replace(r'v\s[a-z]{1,}', 'H')
stats['home-away'] = stats['home-away'].str.replace(r'@\s[a-z]{1,}','A')


stats['opponent'] = stats['opponent'].str.replace('@ ', '')
stats['opponent'] = stats['opponent'].str.replace('v ', '')
stats['opponent'] = stats['opponent'].map(team_lib.dict)



stats['double header'] = stats['double header'].fillna(value=1)
stats['double header'] = stats['double header'].astype('int')

stats['player hand'] = stats['player'].map(player_hand_lib.dict)

stats['opponent runs'] = stats['opponent runs'].str.replace(r'\(.*?\){1,}', '')








stats.to_csv('mlb_season_stat_append_%d.csv' % (append_date), index=0)


