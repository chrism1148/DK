from urllib.request import urlretrieve
import unicodedata
import pandas as pd
import csv #imports module csv
import re


date = 20180331
perfect_game_url_1 = 'https://www.draftkings.com/contest/exportfullstandingscsv/54847274'
perfect_game = 'perfect_game'
perfect_game_entry = 333 

# urlretrieve(perfect_game_url_1, "dk_mlb_%s_%d_raw.csv" % (perfect_game, date))
# data = pd.read_csv('dk_mlb_%s_%d_raw.csv' % (perfect_game, date), sep=',')


data = pd.read_csv('dk_mlb_perfect_game_20180331.csv', sep=',', encoding='ISO-8859-1')
data.columns = ['Rank', 'EntryId', 'EntryName', 'TimeRemaining', 'Points', 'Lineup', 'Null', 'Player', 'RosterPosition', 'PercentDrafted', 'FTPS'] #rename csv colums for proper pandas syntax

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


del data['Null']
# data['Player']         = data['Player'].to_string()
remove_accents(data['Player'].to_string())
data['Rank']           = data.Rank.astype(int)
data['Player']         = data.Player.fillna('NA')
data['RosterPosition'] = data.RosterPosition.fillna('NA')
data['PercentDrafted'] = data.PercentDrafted.fillna('NA')
data['PercentDrafted'] = [p.strip('%') for p in data['PercentDrafted']]
data['FTPS']           = data.FTPS.fillna('0')
data['EntryFee']       = perfect_game_entry
data['Winnings']       = 0
# data['Winnings'][0:7]  = [10000, 6000, 4000, 2000, 1500, 1250, 1250]
# data['Winnings'][7:11] = 1000
# data['Winnings'][11:17]= 750
# data['Winnings'][17:27]= 600
# data['Winnings'][27:48]= 500


data.to_csv('dk_mlb_perfect_game_20180331_formatted.csv', index=False)


