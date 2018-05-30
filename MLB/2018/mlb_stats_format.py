import urllib.request
import csv
import pandas as pd
import os




downloads = '/Users/chrismccallan/Downloads'
formats = ('/Users/chrismccallan/Downloads')

ifile  = os.path.join(downloads, '2018_mlb_full_season.csv')

stats = pd.read_csv(ifile)
stats.columns= ['game_date', 'rotoguru id', 'mlb id', 'player', 'game_started', 'batting order', 'dk position number', 'dk points', 'dk salary', 'team', 'opponent', 'double header', 'team runs', 'opponent runs']


stats['player'] = stats['player'].apply(lambda x: ' '.join(x.split()[::-1]))
stats['team'] = stats['team'].str.lower()



print(stats['player'])
print(stats['team'])


stats.to_csv('mlb_season_stats.csv')


