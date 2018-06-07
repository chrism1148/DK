import player_hand_lib
import player_name_lib
import position_number_lib
import player_position_lib
import team_lib
import pandas as pd
import csv
import os
import re


game_date = 20180607


#HOME
downloads = '/Users/chris/Downloads'
formats = ('/Users/chris/Downloads')


#WORK
# downloads = '/Users/chrismccallan/Downloads'
# formats = ('/Users/chrismccallan/Downloads')


ifile  = os.path.join(downloads, 'gameday_raw_%d.csv' % (game_date))

stats = pd.read_csv(ifile, encoding='ISO-8859-1')
stats.columns= ['player', 'team', 'opponent', 'position', 'salary']


stats['player'] = stats['player'].str.strip()

stats['team'] = stats['team'].str.replace('@', '')
stats['team'] = stats['team'].str.lower()
stats['team'] = stats['team'].map(team_lib.dict)

stats['opponent'] = stats['opponent'].str.replace('@', '')
stats['opponent'] = stats['opponent'].str.lower()
stats['opponent'] = stats['opponent'].map(team_lib.dict)

stats['salary'] = stats['salary'].astype('int')

stats['game_date'] = game_date
stats['player hand'] = stats['player'].map(player_hand_lib.dict)

stats.to_csv('gameday_formatted_%d.csv' % (game_date), index=0)
