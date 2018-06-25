import csv
import re
import unicodedata
import sys
import os
import teamlib


game_date = 20180620



####################    DO NOT CHANGE BELOW THIS LINE  ###########################

#path to file directory - HOME
# formats = ('/Users/Chris/Desktop/Statis/MLB/2018/formats/')

#path to file directory - WORK
downloads = '/Users/chrismccallan/Downloads'
formats = ('/Users/chrismccallan/Downloads')

ifile  = os.path.join(downloads, 'dk_mlb_raw_projections_%d.csv' % (game_date))
ofile  = os.path.join(formats, 'dk_mlb_projection_comparison_upload_%d.csv' % (game_date))
ofile  = open(ofile, 'w')
writer = csv.writer(ofile)


with open(ifile, 'r', encoding='ISO-8859-1') as csvfile:
	reader = csv.reader(csvfile)
	next(reader)

	for row in reader:
		game_date         = game_date
		player            = row[0].strip()
		team_raw          = row[1].strip().lower()
		team_clean        = team_raw.replace('@','')
		opponent_raw      = row[2].strip().lower()
		opponent_clean    = opponent_raw.replace('@','')
		position          = row[3].strip()
		salary            = row[4].strip()
		my_proj           = row[5].strip()
		rotoql_proj       = row[6].strip()
		dfs_guru_proj     = row[7].strip()
		bp_proj           = row[8].strip()
		last_5_games_avg  = row[9].strip()
		season_avg        = row[10].strip()
		dk_points         = row[11].strip()
		# home_away         = re.sub(r'\D[A-Z]{1,}', 'H', row[2])


		for t in team_clean:
			team = teamlib.team_dict[team_clean]

		for o in opponent_clean:
			opponent = teamlib.team_dict[opponent_clean]


		output = (game_date, player, team, opponent, position, salary, my_proj, rotoql_proj, dfs_guru_proj, last_5_games_avg, season_avg, dk_points, bp_proj)
		writer.writerows([output])