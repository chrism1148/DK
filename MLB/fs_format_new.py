import csv #imports python csv module
import re  #imports python regular expressions library
import positionlib

with open('rotoguru_raw_mlb_2017.csv', 'r') as csvfile:
	csvreader = csv.reader(csvfile)  
	next(csvreader)
# ofile  = open('dk_mlb_full_season_2017.csv', 'w') #projection upload to BigQuery
# writer = csv.writer(ofile)

# define fields from RotoGuru MLB CSV
for row in csvreader:
	gid                = row[0] # rotoguru id
	mlb_id             = row[1]
	player             = row[3]
	pitcher_hitter     = row[4]
	hand               = row[5]
	game_date          = row[6]
	team               = row[7]
	opponent           = row[8]
	home_away          = row[9]
	game_number        = row[10] #1 is the first game of the day.  2 is the second game of a doubleheader
	game_id            = row[11]
	game_time          = row[12] #start time in ET
	team_runs          = row[13]
	opponent_runs      = row[14]
	home_umpire        = row[15]
	temperature        = row[16] # in degrees F
	condition          = row[17]
	wind_speed         = row[18]
	wind_direction     = row[19]
	game_started       = row[22]
	game_played        = row[23]
	position           = row[24]
	batting_order      = row[25]
	opp_pitcher_hand   = row[26]
	opp_pitcher_gid    = row[27]
	opp_pitcher_mlb_id = row[28]
	opp_pitcher        = " ".join(row[29].split(',')[::-1]).strip()
	plate_app          = row[30]
	innings_pitched    = row[32]
	decision           = row[33]
	quality_start      = row[34]
	fd_points          = row[35]
	dk_points          = row[36]
	dd_points          = row[37]
	yh_points          = row[38]
	fd_salary          = row[39]
	dk_salary          = row[40]
	yh_salary          = row[42]
	fd_position_num    = row[43]
	dk_position_num    = row[44]
	yh_position_num    = row[46]
	

# Fill blank fields of RotoGuru MLB CSV

	if bool(row[20]) == False:
		ADI          = 0
	else:
		ADI          = row[20] #air density index (Neeley Scale)

	if bool(row[21]) == False:
		prior_ADI    = 0
	else:
		prior_ADI    = row[21] #air density index for prior game

	if bool(row[32]) == False:
		innings_pitched = 0
	else:
		innings_pitched = row[32]

	if bool(row[33]) == False:
		decision     = ('ND')
	else:
		decision     = row[33]

	if bool(row[34])    == False:
		quality_start   = 0 
	else:
		quality_start   = row[34]

	if bool(row[35])    == False:
		fd_points       = 0 
	else:
		fd_points       = row[35]

	if bool(row[36])    == False:
		dk_points       = 0 
	else:
		dk_points       = row[36]

	if bool(row[37])    == False:
		dd_points       = 0 
	else:
		dd_points       = row[37]

	if bool(row[38])    == False:
		yh_points       = 0 
	else:
		yh_points       = row[38]

	if bool(row[39])    == False:
		fd_salary       = 0 
	else:
		fd_salary       = row[39]

	if bool(row[40])    == False:
		dk_salary       = 0 
	else:
		dk_salary       = row[40]

	if bool(row[42])    == False:
		yh_salary       = 0 
	else:
		yh_salary       = row[42]

	if bool(row[43])    == False:
		fd_position_num = 0 
	else:
		fd_position_num = row[43]

	if bool(row[44]) == False:
		dk_position_num = positionlib.position_dict[player]

	if bool(row[46])    == False:
		yh_position_num = 0 
	else:
		yh_position_num = row[46]


# Create dk_position in baseball syntax from position numbers in RotoGuru MLB CSV 

	if dk_position_num   == ('0'):
		dk_position      = ('NA')
	elif dk_position_num   == ('1'):
		dk_position      = ('P')
	elif dk_position_num == ('2'):
		dk_position      = ('C')
	elif dk_position_num == ('3'):
		dk_position      = ('1B')
	elif dk_position_num == ('4'):
		dk_position      = ('2B')
	elif dk_position_num == ('5'):
		dk_position      = ('3B')
	elif dk_position_num == ('6'):
		dk_position      = ('SS')
	elif dk_position_num == ('7'):
		dk_position      = ('OF')
	elif dk_position_num == ('8'):
		dk_position      = ('OF')
	elif dk_position_num == ('9'):
		dk_position      = ('OF')

	elif dk_position_num == ('12'):
		dk_position      = ('P/C')
	elif dk_position_num == ('13'):
		dk_position      = ('P/1B')
	elif dk_position_num == ('14'):
		dk_position      = ('P/2B')
	elif dk_position_num == ('15'):
		dk_position      = ('P/3B')
	elif dk_position_num == ('16'):
		dk_position      = ('P/SS')
	elif dk_position_num == ('17'):
		dk_position      = ('P/OF')
	elif dk_position_num == ('18'):
		dk_position      = ('P/OF')
	elif dk_position_num == ('19'):
		dk_position      = ('P/OF')

	elif dk_position_num == ('21'):
		dk_position      = ('C/P')
	elif dk_position_num == ('23'):
		dk_position      = ('C/1B')
	elif dk_position_num == ('24'):
		dk_position      = ('C/2B')
	elif dk_position_num == ('25'):
		dk_position      = ('C/3B')
	elif dk_position_num == ('26'):
		dk_position      = ('C/SS')
	elif dk_position_num == ('27'):
		dk_position      = ('C/OF')
	elif dk_position_num == ('28'):
		dk_position      = ('C/OF')
	elif dk_position_num == ('29'):
		dk_position      = ('C/OF')
	
	elif dk_position_num == ('31'):
		dk_position      = ('1B/P')
	elif dk_position_num == ('32'):
		dk_position      = ('1B/C')
	elif dk_position_num == ('34'):
		dk_position      = ('1B/2B')
	elif dk_position_num == ('35'):
		dk_position      = ('1B/3B')
	elif dk_position_num == ('36'):
		dk_position      = ('1B/SS')
	elif dk_position_num == ('37'):
		dk_position      = ('1B/OF')
	elif dk_position_num == ('38'):
		dk_position      = ('1B/OF')
	elif dk_position_num == ('39'):
		dk_position      = ('1B/OF')

	elif dk_position_num == ('41'):
		dk_position      = ('2B/P')
	elif dk_position_num == ('42'):
		dk_position      = ('2B/C')
	elif dk_position_num == ('43'):
		dk_position      = ('2B/1B')
	elif dk_position_num == ('45'):
		dk_position      = ('2B/3B')
	elif dk_position_num == ('46'):
		dk_position      = ('2B/SS')
	elif dk_position_num == ('47'):
		dk_position      = ('2B/OF')
	elif dk_position_num == ('48'):
		dk_position      = ('2B/OF')
	elif dk_position_num == ('49'):
		dk_position      = ('2B/OF')
	
	elif dk_position_num == ('51'):
		dk_position      = ('3B/P')
	elif dk_position_num == ('52'):
		dk_position      = ('3B/C')
	elif dk_position_num == ('53'):
		dk_position      = ('3B/1B')
	elif dk_position_num == ('54'):
		dk_position      = ('3B/2B')
	elif dk_position_num == ('56'):
		dk_position      = ('3B/SS')
	elif dk_position_num == ('57'):
		dk_position      = ('3B/OF')
	elif dk_position_num == ('58'):
		dk_position      = ('3B/OF')
	elif dk_position_num == ('59'):
		dk_position      = ('3B/OF')

	elif dk_position_num == ('61'):
		dk_position      = ('SS/P')
	elif dk_position_num == ('62'):
		dk_position      = ('SS/C')
	elif dk_position_num == ('63'):
		dk_position      = ('SS/1B')
	elif dk_position_num == ('64'):
		dk_position      = ('SS/2B')
	elif dk_position_num == ('65'):
		dk_position      = ('SS/3B')
	elif dk_position_num == ('67'):
		dk_position      = ('SS/OF')
	elif dk_position_num == ('68'):
		dk_position      = ('SS/OF')
	elif dk_position_num == ('69'):
		dk_position      = ('SS/OF')
	 
	elif dk_position_num == ('71'):
		dk_position      = ('OF/P')
	elif dk_position_num == ('72'):
		dk_position      = ('OF/C')
	elif dk_position_num == ('73'):
		dk_position      = ('OF/1B')
	elif dk_position_num == ('74'):
		dk_position      = ('OF/2B')
	elif dk_position_num == ('75'):
		dk_position      = ('OF/3B')
	elif dk_position_num == ('76'):
		dk_position      = ('OF/SS')
	elif dk_position_num == ('78'):
		dk_position      = ('OF')
	elif dk_position_num == ('79'):
		dk_position      = ('OF')

	elif dk_position_num == ('81'):
		dk_position      = ('OF/P')
	elif dk_position_num == ('82'):
		dk_position      = ('OF/C')
	elif dk_position_num == ('83'):
		dk_position      = ('OF/1B')
	elif dk_position_num == ('84'):
		dk_position      = ('OF/2B')
	elif dk_position_num == ('85'):
		dk_position      = ('OF/3B')
	elif dk_position_num == ('86'):
		dk_position      = ('OF/SS')
	elif dk_position_num == ('87'):
		dk_position      = ('OF')
	elif dk_position_num == ('89'):
		dk_position      = ('OF')

	elif dk_position_num == ('91'):
		dk_position      = ('OF/P')
	elif dk_position_num == ('92'):
		dk_position      = ('OF/C')
	elif dk_position_num == ('93'):
		dk_position      = ('OF/1B')
	elif dk_position_num == ('94'):
		dk_position      = ('OF/2B')
	elif dk_position_num == ('95'):
		dk_position      = ('OF/3B')
	elif dk_position_num == ('96'):
		dk_position      = ('OF/SS')
	elif dk_position_num == ('97'):
		dk_position      = ('OF')
	elif dk_position_num == ('98'):
		dk_position      = ('OF')
	else:
		dk_position      = ('NA')

# RotoGuru player names

	output = (gid,
	mlb_id,
	player,
	pitcher_hitter,
	hand,
	game_date,
	team,
	opponent,
	home_away,
	game_number,
	game_id,
	game_time,
	team_runs,
	opponent_runs,
	home_umpire,
	temperature,
	condition,
	wind_speed,
	wind_direction,
	game_started,
	game_played,
	position,
	batting_order,
	opp_pitcher_hand,
	opp_pitcher_gid,
	opp_pitcher_mlb_id,
	opp_pitcher,
	plate_app,
	innings_pitched,
	decision,
	quality_start,
	fd_points,
	dk_points,
	dd_points,
	yh_points,
	fd_salary,
	dk_salary,
	yh_salary,
	fd_position_num,
	dk_position_num,
	dk_position,
	yh_position_num,)


	writer.writerows([output])

