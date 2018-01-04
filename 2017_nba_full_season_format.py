import csv #imports module csv
import re

ifile  = open('nba_season_2017.csv', 'r') #RotoGuru player csv export
reader = csv.reader(ifile, delimiter=',')
ofile  = open('nba_full_season_2017_formatted_test.csv', 'w') #projection upload to BigQuery
writer = csv.writer(ofile, delimiter = ',')


for row in reader:
	player_id       = row[0]
	# if bool(row[1]) == False:
	# 	nba_id      = 0
	# else:
	# 	nba_id      = row[]
	player            = row[2]
	game_date         = row[3]
	team              = row[4]
	opponent          = row[5]
	home_away		  = row[6]
	game_id           = row[7]
	team_points       = row[8]
	opponent_points   = row[9]
	game_started      = row[10]
	game_minutes	  = row[11]
	game_played       = row[12]
	game_active       = row[13]
	
	fd_points         = row[14]
	dk_points         = row[15]
	# try:
	# 	dk_points     =[float(row[15]) for x in row[15]]
	# except ValueError:
	# 	print ("error",e,"on line",i)
	dd_points         = row[16]
	yh_points         = row[17]
	
	fd_salary         = row[18]
	fd_salary_change  = row[19]
	dk_salary         = row[20]
	dk_salary_change  = row[21]
	# dd_salary         = row[22]
	# dd_salary_change  = row[23]
	yh_salary         = row[22]
	yh_salary_change  = row[23]

	fd_position       = row[24]
	dk_position       = row[25]
	# dd_position       = row[28]
	yh_position       = row[26]

	double_double     = row[27]
	triple_double     = row[28]

	stats             = row[29].replace('pt',' points,')
	stats             = stats.replace('as', ' assist,')
	stats             = stats.replace('rb', ' rebound,')
	stats             = stats.replace('to', ' to,')
	stats             = stats.replace('trey', ' trey,')
	stats             = stats.replace('st ', ' steal,')
	stats             = stats.replace('bl ', ' block,')
	stats             = stats.replace('fg ', ' fg,')
	stats             = stats.replace('ft ', ' ft,')



	# game_rebounds   = row[20]
	# game_assists    = row[21]
	# game_steals     = row[22]
	# game_blocks     = row[23]
	# game_turnovers  = row[24]
	

# RotoGuru (matching rotoguru.com)
	# team  = team.replace("ny","nyk")
	# team  = team.replace("no", "nor")
	# team  = team.replace("gs", "gsw")
	# team  = team.replace("sa", "sas")
	# team  = team.replace("sasc", "sac")
	
	# opponent = opponent.replace("ny", "nyk")
	# opponent = opponent.replace("no", "nor")
	# opponent = opponent.replace("gs", "gsw")
	# opponent = opponent.replace("sa", "sas")
	# opponent = opponent.replace("sasc", "sac")

# RotoGuru player names
	player = player.replace("AJ Hammons", "A.J. Hammons")
	player = player.replace("CJ McCollum", "C.J. McCollum")
	player = player.replace("CJ Miles", "C.J. Miles")
	player = player.replace("CJ Wilcox", "C.J. Wilcox")
	player = player.replace("Ish Smith", "Ishmael Smith")
	player = player.replace("James Ennis III", "James Ennis")
	player = player.replace("J.J. Barea", "Jose Barea")
	player = player.replace("JJ Redick", "J.J. Redick")
	player = player.replace("JR Smith", "J.R. Smith")
	player = player.replace("Kelly Oubre Jr.", "Kelly Oubre")
	player = player.replace("KJ McDaniels", "K.J. McDaniels")
	player = player.replace("Nene", "Nene Hilario")
	player = player.replace("Otto Porter Jr.", "Otto Porter")
	player = player.replace("PJ Tucker", "P.J. Tucker")
	player = player.replace("TJ Warren", "T.J. Warren")
	player = player.replace("Wesley Matthews", "Wes Matthews")
	player = player.replace("Willy Hernangomez", "Guillermo Hernangomez")


	output = (player_id, player, game_date, team, opponent, home_away, team_points, opponent_points, game_started, game_minutes, game_played, game_active, dk_points, dk_position, dk_salary, dk_salary_change, double_double, triple_double, stats)
	writer.writerows([output])


ifile.close()
ofile.close()