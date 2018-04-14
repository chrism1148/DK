import csv
import re
import unicodedata
import sys
import os
import teamlib



####################    DO NOT CHANGE BELOW THIS LINE  ###########################

game_date = 20180408

downloads = '/Users/chris/Downloads'
formats = ('/Users/Chris/Desktop/Statis/MLB/2018/formats/')
# formats = ('/Users/chrismccallan/Downloads')

ifile  = os.path.join(downloads, 'csv2.csv')
ofile  = os.path.join(formats, 'dk_mlb_projection_comparison_upload_%d.csv' % (game_date))
ofile  = open(ofile, 'w')
writer = csv.writer(ofile)


with open(ifile, 'r') as csvfile:
	reader = csv.reader(csvfile)
	next(reader)

	for row in reader:
		game_date         = row[0]
		player            = row[1].strip()
		team_raw          = row[2].strip().lower()
		team_clean        = team_raw.replace('@','')
		opponent_raw      = row[3].strip().lower()
		opponent_clean    = opponent_raw.replace('@','')
		position          = row[4].strip()
		salary            = row[5].strip()
		my_proj           = row[6].strip()
		rotoql_proj       = row[7].strip()
		dfs_guru_proj     = row[8].strip()
		last_5_games_avg  = row[9].strip()
		season_avg        = row[10].strip()
		dk_points         = row[11].strip()
		# home_away         = re.sub(r'\D[A-Z]{1,}', 'H', row[2])


		for t in team_clean:
			team = teamlib.team_dict[team_clean]

		for o in opponent_clean:
			opponent = teamlib.team_dict[opponent_clean]

		# for opponent in opponent:
		# 	opponent = teamlib.team_dict[opponent]


		output = (game_date, player, team, opponent, position, salary, my_proj, rotoql_proj, dfs_guru_proj, last_5_games_avg, season_avg, dk_points)
		# print(team)
		writer.writerows([output])

