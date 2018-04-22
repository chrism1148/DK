import pandas as pd
import re
import csv
import os


contest_date = 20180410
contest_name = 'silver_slugger'
contest_entry_fee = 1060
contest_id = 55265054





################################## START OF NO CHANGE POLICY ##############################

#path to files - HOME
formats = ('/Users/Chris/downloads/')
uploads = ('/Users/Chris/downloads/')

 #path to files - WORK
# formats = ('/Users/chrismccallan/downloads/')
# uploads = ('/Users/chrismccallan/downloads/')

ifile   = os.path.join(formats, 'dk_mlb_%s_%d_formatted.csv' % (contest_name, contest_date))
ofile   = os.path.join(uploads, 'dk_mlb_%s_%d_upload.csv' % (contest_name, contest_date))

data = pd.read_csv(ifile)
data.columns = ['Rank', 'EntryId', 'EntryName', 'EntryPoints', 'Player', 'Position', 'PercentDrafted', 'PlayerPoints', 'Pitcher1', 'Pitcher2', 'Catcher', 'FirstBase', 'SecondBase', 'ThirdBase', 'ShortStop', 'Outfield'] #rename csv colums for proper pandas syntax


data['Rank']           = data['Rank'].fillna(0)
data['EntryId']        = data['EntryId'].fillna(0)
data['EntryName']      = data['EntryName'].fillna('nan')
data['EntryPoints']    = data['EntryPoints'].fillna(0)

data['Player']         = data.Player.fillna('NA')
data['Player']         = data['Player'].str.replace('Michael A. Taylor', 'Michael Taylor')

data['Position']       = data.Position.fillna('NA')
data['PercentDrafted'] = data.PercentDrafted.fillna('0')
data['PlayerPoints']   = data.PlayerPoints.fillna('0')

data['Pitcher1']       = data.Pitcher1.fillna('nan')
data['Pitcher2']       = data.Pitcher2.fillna('nan')
data['Catcher']        = data.Catcher.fillna('nan')
data['FirstBase']      = data.FirstBase.fillna('nan')
data['SecondBase']     = data.SecondBase.fillna('nan')
data['ThirdBase']      = data.ThirdBase.fillna('nan')
data['ShortStop']      = data.ShortStop.fillna('nan')

data['Outfield1']      = data['Outfield'].astype(str).str.split(',').str[0].fillna('nan') #regex from the format feed script shortens Michael A. Taylor to Michael A.
data['Outfield1']      = data['Outfield1'].str.replace('Michael A.', 'Michael Taylor')
data['Outfield2']      = data['Outfield'].astype(str).str.split(',').str[1].fillna('nan')
data['Outfield2']      = data['Outfield2'].str.replace('Michael A.', 'Michael Taylor')
data['Outfield3']      = data['Outfield'].astype(str).str.split(',').str[2].fillna('nan')
data['Outfield3']      = data['Outfield3'].str.replace('Michael A.', 'Michael Taylor')

del data['Outfield']

data['ContestDate']    = contest_date
data['ContestName']    = contest_name
data['ContestId']      = contest_id
data['ContestFee']     = contest_entry_fee


################################## END OF NO CHANGE POLICY ##############################

data['Winnings']            = 0
data.loc[0:0, 'Winnings']   = 1000
# data.loc[7:9, 'Winnings']    = 500
# data.loc[10:16, 'Winnings']  = 400
# data.loc[17:25, 'Winnings']  = 300
# data.loc[26:41, 'Winnings']  = 250


# data['Winnings']             = 0
# data.loc[0:9, 'Winnings']    = [50000, 25000, 15000, 10000, 7000, 6000, 5000, 5000, 4000, 4000]
# data.loc[10:14, 'Winnings']  = 3500
# data.loc[15:19, 'Winnings']  = 3000
# data.loc[20:24, 'Winnings']  = 2500
# data.loc[25:34, 'Winnings']  = 2000
# data.loc[35:49, 'Winnings']  = 1500
# data.loc[50:68, 'Winnings']  = 1000
# data.loc[69:98, 'Winnings']  = 800
# data.loc[99:153, 'Winnings']  = 700

# print(data.iloc[108, data.columns.get_loc('Player')])

data.to_csv(ofile, index=None)