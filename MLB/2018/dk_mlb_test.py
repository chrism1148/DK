import csv
import re
import unicodedata
import pandas as pd

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


ifile  = ('dk_mlb_perfect_game_20180331.csv')
ofile  = open('dk_mlb_perfect_game_dataframe.csv', 'w') 
writer = csv.writer(ofile)


with open(ifile, 'r') as csvfile:
	reader = csv.reader(csvfile)
	next(reader)

	for row in reader:
		rank              = row[0]
		entry_id          = row[1]
		entry_name        = row[2]
		lineup_points     = row[4]
		player            = remove_accents(row[7])
		player_position   = row[8]
		player_percentage = row[9].replace('%', '')
		player_points     = row[10]
		lineup            = remove_accents(row[5])
		# pitcher           = re.match(r'^[a-z\sA-Z ]+$', lineup)


		output = (rank, entry_id, entry_name, lineup_points, player, player_position, player_percentage, player_points, lineup)
		writer.writerows([output])

		print(pitcher)


# date = 20180331
# perfect_game_url_1 = 'https://www.draftkings.com/contest/exportfullstandingscsv/54847274'
# perfect_game = 'perfect_game'
# perfect_game_entry = 333 

# # urlretrieve(perfect_game_url_1, "dk_mlb_%s_%d_raw.csv" % (perfect_game, date))
# # data = pd.read_csv('dk_mlb_%s_%d_raw.csv' % (perfect_game, date), sep=',')

# data = pd.read_csv('dk_mlb_perfect_game_dataframe.csv', sep=',')
# data.columns = ['Rank', 'EntryId', 'EntryName', 'Points', 'Lineup', 'Null', 'Player', 'RosterPosition', 'PercentDrafted', 'FTPS'] #rename csv colums for proper pandas syntax


# del data['Null']
# data['Rank']           = data.Rank.astype(int)
# data['Player']         = data.Player.fillna('NA')

# data['RosterPosition'] = data.RosterPosition.fillna('NA')
# data['PercentDrafted'] = data.PercentDrafted.fillna('NA')
# data['PercentDrafted'] = [p.strip('%') for p in data['PercentDrafted']]
# data['FTPS']           = data.FTPS.fillna('0')
# data['EntryFee']       = perfect_game_entry
# # data['Winnings']       = 0
# # data['Winnings'][0:7]  = [10000, 6000, 4000, 2000, 1500, 1250, 1250]
# # data['Winnings'][7:11] = 1000
# # data['Winnings'][11:17]= 750
# # data['Winnings'][17:27]= 600
# # data['Winnings'][27:48]= 500


# data.to_csv('dk_mlb_perfect_game_20180331_formatted.csv', index=False)
