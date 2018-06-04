import urllib.request
import csv
import pandas as pd
import os
import player_hand_lib as phl
import player_name_lib as pnl



downloads = '/Users/chrismccallan/Downloads'
formats = ('/Users/chrismccallan/Downloads')

ifile  = os.path.join(downloads, '2018_mlb_full_season.csv')

stats = pd.read_csv(ifile)
stats.columns= ['game_date', 'rotoguru id', 'mlb id', 'player', 'starter', 'batting order', 'dk position number', 'dk points', 'dk salary', 'team', 'opponent', 'double header', 'team runs', 'opponent runs']


stats['player'] = stats['player'].apply(lambda x: ' '.join(x.split(',')[::-1]))
stats['player'] = stats['player'].str.strip()
stats['player'] = stats['player'].map(pnl.dict)

stats['starter'] = stats['starter'].fillna(value=0)
stats['starter'] = stats['starter'].astype('int')


stats['team'] = stats['team'].str.lower()
stats['opponent'] = stats['opponent'].str.replace('@ ', '')
stats['opponent'] = stats['opponent'].str.replace('v ', '')


stats['double header'] = stats['double header'].fillna(value=0)
stats['double header'] = stats['double header'].astype('int')


stats['player hand'] = stats['player'].map(phl.dict)




print(stats['player hand'])


stats.to_csv('mlb_season_stats.csv')


