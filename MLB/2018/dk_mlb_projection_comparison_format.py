import csv
import re
import unicodedata
import sys
import os



####################    DO NOT CHANGE BELOW THIS LINE  ###########################

game_date = 20180407

downloads = '/Users/chrismccallan/Downloads'
# formats = ('/Users/Chris/Desktop/Statis/MLB/2018/formats/')
formats = ('/Users/chrismccallan/Downloads')

ifile  = os.path.join(downloads, 'csv2.csv')
ofile  = os.path.join(formats, 'dk_mlb_projection_comparision_upload_%d.csv' % (game_date))
ofile  = open(ofile, 'w')
writer = csv.writer(ofile)


with open(ifile, 'r') as csvfile:
	reader = csv.reader(csvfile)
	# next(reader)

	for row in reader:
		game_date         = row[0]
		player            = row[1].strip()
		team              = row[2].strip().lower()
		opponent          = row[3].strip().lower()
		position          = row[4].strip()
		salary            = row[5].strip()
		my_proj           = row[6].strip()
		rotoql_proj       = row[7].strip()
		dfs_guru_proj     = row[8].strip()
		last_5_games_avg  = row[9].strip()
		season_avg        = row[10].strip()
		dk_points         = row[11].strip()
		home_away         = re.sub(r'\D[A-Z]{1,}', 'H', row[2])

		print(home_away)
	

		output = (game_date, player, team, opponent, position, salary, my_proj, rotoql_proj, dfs_guru_proj, last_5_games_avg, season_avg, dk_points)
		writer.writerows([output])

