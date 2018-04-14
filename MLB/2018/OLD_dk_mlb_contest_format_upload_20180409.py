import pandas as pd
import re
import csv


contest_date = 20180409
contest_name = 'fielders_choice'
contest_entry_fee = 50
contest_id = 55231523
# perfect_game_url_1 = 'https://www.draftkings.com/contest/exportfullstandingscsv/54847274'

# urlretrieve(perfect_game_url_1, "dk_mlb_%s_%d_raw.csv" % (perfect_game, date))
# data = pd.read_csv('dk_mlb_%s_%d_raw.csv' % (perfect_game, date), sep=',')

data = pd.read_csv('dk_mlb_%s_%d_formatted.csv' % (contest_name, contest_date))
data.columns = ['Rank', 'EntryId', 'EntryName', 'EntryPoints', 'Player', 'Position', 'PercentDrafted', 'PlayerPoints', 'Pitcher1', 'Pitcher2', 'Catcher', 'FirstBase', 'SecondBase', 'ThirdBase', 'ShortStop', 'Outfield'] #rename csv colums for proper pandas syntax

data['Rank']           = data['Rank'].fillna(0)
data['EntryId']        = data['EntryId'].fillna(0)
data['EntryName']      = data['EntryName'].fillna('NA')
data['EntryPoints']    = data['EntryPoints'].fillna(0)

data['Player']         = data.Player.fillna('NA')
data['Position']       = data.Position.fillna('NA')
data['PercentDrafted'] = data.PercentDrafted.fillna('0')
data['PlayerPoints']   = data.PlayerPoints.fillna('0')

data['Pitcher1']       = data.Pitcher1.fillna('NA')
data['Pitcher2']       = data.Pitcher2.fillna('NA')
data['Catcher']        = data.Catcher.fillna('NA')
data['FirstBase']      = data.FirstBase.fillna('NA')
data['SecondBase']     = data.SecondBase.fillna('NA')
data['ThirdBase']      = data.ThirdBase.fillna('NA')
data['ShortStop']      = data.ShortStop.fillna('NA')

data['Outfield1']      = data['Outfield'].astype(str).str.split(',').str[0]
data['Outfield2']      = data['Outfield'].astype(str).str.split(',').str[1]
data['Outfield3']      = data['Outfield'].astype(str).str.split(',').str[2]
data['Outfield1']      = data.Outfield1.fillna('NA')
data['Outfield2']      = data.Outfield2.fillna('NA')
data['Outfield3']      = data.Outfield3.fillna('NA')
del data['Outfield']

data['ContestDate']    = contest_date
data['ContestName']    = contest_name
data['ContestId']      = contest_id
data['ContestFee']     = contest_entry_fee

data['Winnings']             = 0
data.loc[0:5, 'Winnings']    = [500, 400, 350, 300, 250, 200]
data.loc[6:10, 'Winnings']    = 100
# data.loc[16:27, 'Winnings']   = 75
# data.loc[13:24, 'Winnings']  = 3500
# data.loc[25:34, 'Winnings']  = 800
# data.loc[35:49, 'Winnings']  = 700
# data.loc[50:69, 'Winnings']  = 600
# data.loc[70:121, 'Winnings'] = 500


# print(data['Rank'], data['EntryName'], data['Winnings'])

data.to_csv('dk_mlb_%s_%d_upload.csv' % (contest_name, contest_date), index=None)
