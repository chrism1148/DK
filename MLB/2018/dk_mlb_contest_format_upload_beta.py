import pandas as pd
import re
import csv
import os
import playerlib



contest_date = 20180509
contest_name = 'three_thousand_hit_club'
contest_entry_fee = 3000
contest_id = 56221206



################################## START OF NO CHANGE POLICY ##############################

#path to files - HOME
formats = ('/Users/Chris/downloads/')
uploads = ('/Users/Chris/downloads/')

 #path to files - WORK
# formats = ('/Users/chrismccallan/downloads/')
# uploads = ('/Users/chrismccallan/downloads/')

ifile   = os.path.join(formats, 'contest-standings-%d.csv' % (contest_id))
ofile   = os.path.join(uploads, 'dk_mlb_%s_%d_%d_upload.csv' % (contest_name, contest_id, contest_date))

data = pd.read_csv(ifile)
data.columns = ['Rank', 'EntryId', 'EntryName', 'Time Remaining', 'EntryPoints', 'Lineup', 'Empty', 'Player', 'Position', 'PercentDrafted', 'PlayerPoints']

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


data.fillna('0')

data['Rank']           = data['Rank'].fillna(0)
data['EntryId']        = data['EntryId'].fillna(0)
data['EntryName']      = data['EntryName'].fillna('nan')
data['EntryPoints']    = data['EntryPoints'].fillna(0)

data['Player']         = data.Player.fillna('NA')
data['Position']       = data.Position.fillna('NA')
data['PercentDrafted'] = data.PercentDrafted.fillna('0')
data['PlayerPoints']   = data.PlayerPoints.fillna('0')


# data['Pitcher1']       = data.Pitcher1.fillna('nan')
# data['Pitcher2']       = data.Pitcher2.fillna('nan')
# data['Catcher']        = data.Catcher.fillna('nan')
# data['FirstBase']      = data.FirstBase.fillna('nan')
# data['SecondBase']     = data.SecondBase.fillna('nan')
# data['ThirdBase']      = data.ThirdBase.fillna('nan')
# data['ShortStop']      = data.ShortStop.fillna('nan')

# data['Outfield1']      = data['Outfield'].astype(str).str.split(',').str[0] # split outfield string into separate columns
# data['Outfield1']      = data.Outfield1.map(playerlib.player_dict) #  replace with dictionary value 
# data['Outfield1']      = data.Outfield1.fillna('nan') # fill empty space with 'nan'

# data['Outfield2']      = data['Outfield'].astype(str).str.split(',').str[1]
# data['Outfield2']      = data.Outfield2.map(playerlib.player_dict)
# data['Outfield2']      = data.Outfield2.fillna('nan')

# data['Outfield3']      = data['Outfield'].astype(str).str.split(',').str[2]
# data['Outfield3']      = data.Outfield3.map(playerlib.player_dict)
# data['Outfield3']      = data.Outfield3.fillna('nan')

# del data['Outfield']

# data['ContestDate']    = contest_date
# data['ContestName']    = contest_name
# data['ContestId']      = contest_id
# data['ContestFee']     = contest_entry_fee


################################## END OF NO CHANGE POLICY ##############################



# data['Winnings']              = 0
# data.loc[0:5, 'Winnings']     = (100000, 50000, 25000, 15000, 10000, 10000)
# data.loc[6:9, 'Winnings']     = 7500
# data.loc[10:21, 'Winnings']   = 5000
# data.loc[25:49, 'Winnings']   = 350
# data.loc[50:93, 'Winnings']   = 250
# data.loc[58:92, 'Winnings']   = 1000
# data.loc[93:167, 'Winnings']  = 850


data.to_csv(ofile, index=None)