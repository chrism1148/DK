from urllib.request import urlretrieve
import pandas as pd
import csv #imports module csv
import re


date = 20180331
# thunder_dome_id_1 = 
perfect_game_id_1 = 54847274
# contest_id_2 = 
# contest_id_1 =
# contest_id_2 = 
# contest_id_1 =
# contest_id_2 = 

# thunder_dome_url_1 = 'https://www.draftkings.com/contest/exportfullstandingscsv/%d' (contest_id_1)
# thunder_dome = 'thunder_dome'

perfect_game_url_1 = 'https://www.draftkings.com/contest/exportfullstandingscsv/%d' % (perfect_game_id_1)
perfect_game = 'perfect_game'
perfect_game_entry = 333
# perfect_game 


urlretrieve(perfect_game_url_1, "dk_mlb_%s_%d_raw.csv" % (perfect_game, date))

data = pd.read_csv('dk_mlb_%s_%d_raw.csv' % (perfect_game, date), sep='delimiter', axis=1)
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