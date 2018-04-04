from urllib.request import urlretrieve
import pandas as pd
import csv #imports module csv
import re


date = 20180331
perfect_game_url_1 = 'https://www.draftkings.com/contest/exportfullstandingscsv/54847274'
perfect_game = 'perfect_game'
perfect_game_entry = 333
# perfect_game 


urlretrieve(perfect_game_url_1, "dk_mlb_%s_%d_raw.csv" % (perfect_game, date))

data = pd.read_csv('dk_mlb_%s_%d_raw.csv' % (perfect_game, date), sep=',')
data.columns = ['Rank', 'EntryId', 'EntryName', 'TimeRemaining', 'Points', 'Lineup', 'Null', 'Player', 'RosterPosition', 'PercentDrafted', 'FTPS'] #rename csv colums for proper pandas syntax

del data['Null']
data['Rank']           = data.Rank.astype(int)
data['Player']         = data.Player.fillna('NA')
data['RosterPosition'] = data.RosterPosition.fillna('NA')
data['PercentDrafted'] = data.PercentDrafted.fillna('NA')
data['PercentDrafted'] = [p.strip('%') for p in data['PercentDrafted']]
data['FTPS']           = data.FTPS.fillna('0')
data['EntryFee']       = perfect_game_entry
data['Winnings']       = 0

 
data.to_csv('dk_mlb_perfect_game_20180331_formatted.csv', index=False)