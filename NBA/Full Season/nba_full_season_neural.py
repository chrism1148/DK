import csv #imports module csv
import re

ifile  = open('nba_full_season_2016_formatted.csv', 'r') #RotoGuru player csv export
reader = csv.reader(ifile, delimiter=',')
ofile  = open('nba_full_season_2016_formatted_test.csv', 'w') #projection upload to BigQuery
writer = csv.writer(ofile, delimiter = ',')


for row in reader:
	player_id         = row[0]
	player            = row[1]
	game_date         = row[2]
	team              = row[3]
	opponent          = row[4]
	home_away		  = row[5]
	team_points       = int(row[6])
	opponent_points   = int(row[7])
	game_started      = int(row[8])
	game_minutes	  = int(row[9])
	game_played       = int(row[10])
	game_active       = int(row[11])
	dk_points         = int(row[12])
	# try:
	# 	dk_points     =[float(row[15]) for x in row[15]]
	# except ValueError:
	# 	print ("error",e,"on line",i)
	dk_position       = int(row[13])
	dk_salary         = int(row[14])
	dk_salary_change  = int(row[15])
	double_double     = int(row[16])
	triple_double     = int(row[17])
	points            = int(row[18])
	rebounds          = int(row[19])
	assists           = int(row[20])
	steals            = int(row[21])
	blocks            = int(row[22])
	turnovers         = int(row[23])
	threes            = int(row[24])
	field_goals_made  = int(row[25])
	field_goals_att   = int(row[26])
	free_throws_made  = int(row[27])
	free_throws_att   = int(row[28])


	


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


	output = (player_id, player, game_date, team, opponent, home_away, team_points, opponent_points, game_started, game_minutes, game_played, game_active, 
		      dk_points, dk_position, dk_salary, dk_salary_change, double_double, triple_double, points, rebounds, assists, steals,  blocks, turnovers, threes, field_goals_made, field_goals_att, free_throws_made, free_throws_att)
	writer.writerows([output])

print(type(player_id))
print(type(player))
print(type(game_date))
print(type(team))
print(type(opponent))
print(type(home_away))
print(type(team_points))
print(type(opponent_points))
print(type(game_started))
print(type(game_minutes))
print(type(game_played))
print(type(game_active))
print(type(dk_points))
print(type(dk_position))
print(type(dk_salary)) 
print(type(dk_salary_change))
print(type(double_double))
print(type(triple_double))
print(type(points))
print(type(rebounds))
print(type(assists))
print(type(steals))
print(type(blocks))
print(type(turnovers))
print(type(threes))
print(type(field_goals_made))
print(type(field_goals_att))
print(type(free_throws_made))
print(type(free_throws_att))





ifile.close()
ofile.close()