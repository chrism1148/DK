import csv #imports module csv
import re
import nba_positionlib

ifile  = open('dk_nba_gameday_20171128_formatted.csv', 'r') #RotoGuru player csv export
reader = csv.reader(ifile, delimiter=',')
ofile  = open('dk_salary_20171128_bq_upload.csv', 'w') #projection upload to BigQuery
writer = csv.writer(ofile, delimiter = ',')


for row in reader:
	game_date     = '20171127'
	position      = row[0]
	player        = row[1]
	salary        = row[2]
	remove        = ' '
	matchup       = row[3].split(remove, 1)[0]      
	# avg_dk_points = row[5]
	
	# multiplier    = (float(avg_dk_points)/((int(salary)/1000)))
	# multiplier    = round(multiplier,2)
	
	# team          = row[6].lower()
	# if row[3].lower() == team:
	# 	opponent = row[4].lower()
	# else:
	# 	opponent = row[3].lower()

# RotoGuru (matching rotoguru.com)
	team  = team.replace("ny","nyk")
	team  = team.replace("no", "nor")
	team  = team.replace("gs", "gsw")
	team  = team.replace("sa", "sas")
	team  = team.replace("sasc", "sac")
	
	opponent  = opponent.replace("ny","nyk")
	opponent  = opponent.replace("no", "nor")
	opponent  = opponent.replace("gs", "gsw")
	opponent  = opponent.replace("sa", "sas")
	opponent  = opponent.replace("sasc", "sac")

	if team == row[3].lower():
		home_away = 'a'
	else:
		home_away = 'h'

	position_num = nba_positionlib.position_dict[position]
		

	output = (matchup)	
	# output = (game_date, position, position_num, player, salary, team, opponent, home_away, avg_dk_points, multiplier)
	writer.writerows([output])


ifile.close()
ofile.close()