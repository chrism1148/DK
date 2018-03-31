import csv #imports python csv module
import re  #imports python regular expressions library
import numpy as np
import pandas as pd

ifile  = 'Workbook.csv'
ofile  = 'dk_mlb_gameday_20170727.csv' #gameday data upload to BigQuery

data = pd.read_csv(ifile, sep=',', encoding='ISO-8859-1', na_values='NaN', header=None) #RotoQL player csv export
df = pd.DataFrame(data)
pitcher_team = df.iloc[:,[0]]
pitcher_opponent= df.iloc[:,[1]]
team_pitcher = df.iloc[:, 2]
opponent_pitcher = df.iloc[:, 3]


df.to_csv(ofile, index=False)


# Change teams to abbreviations
for team in pitcher_team:
	if team == 'New York Yankees':
		pitcher_team  = 'nyy'
	if team == 'Boston':
		team      = 'bos'
	if team == 'Baltimore':
		team      = 'bal'
	if team == 'Tampa Bay':
		team      = 'tam'
	if team == 'Toronto':
		team      = 'tor'

	if team == 'Texas':
		team      = 'tex'
	if team == 'Los Angeles Angels':
		pitcher_team = 'laa'
	if team == 'Houston':
		team      = 'hou'
	if team == 'Oakland':
		team      = 'oak'
	if team == 'Seattle':
		team      = 'sea'

	if team == 'Kansas City':
		team      = 'kan'
	if team == 'Minnesota':
		team      = 'min'
	if team == 'Chicago Sox':
		team      = 'chw'
	if team == 'Cleveland':
		team      = 'cle'
	if team == 'Detroit':
		team      = 'det'

	if team == 'New York Mets':
		team      = 'nym'
	if team == 'Atlanta':
		team      = 'atl'
	if team == 'Miami':
		team      = 'mia'
	if team == 'Washington':
		team      = 'was'
	if team == 'Philadelphia':
		team      = 'phi'

	if team == 'Chicago Cubs':
		team      = 'chc'
	if team == 'St. Louis':
		team      = 'stl'
	if team == 'Pittsburgh':
		team      = 'pit'
	if team == 'Milwaukee':
		team      = 'mil'
	if team == 'Cincinnati':
		team      = 'cin'

	if team == 'San Francisco':
		team      = 'sfo'
	if team == 'Los Angeles Dodgers':
		team      = 'lad'
	if team == 'Arizona':
		pitcher_team  = 'ari'
	if team == 'San Diego':
		team      = 'sdg'
	if team == 'Colorado':
		team      = 'col'

df.to_csv(ofile, index=False)

# 	if opponent in ('New York Yankees':
# 		opponent  = ('nyy'
# 	if opponent in ('Boston':
# 		opponent  = ('bos'
# 	if opponent in ('Baltimore':
# 		opponent  = ('bal'
# 	if opponent in ('Tampa Bay':
# 		opponent  = ('tam'
# 	if opponent in ('Toronto':
# 		opponent  = ('tor'

# 	if opponent in ('Texas':
# 		opponent  = ('tex'
# 	if opponent in ('Los Angeles Angels':
# 		opponent  = ('laa'
# 	if opponent in ('Houston':
# 		opponent  = ('hou'
# 	if opponent in ('Oakland':
# 		opponent  = ('oak'
# 	if opponent in ('Seattle':
# 		opponent  = ('sea'

# 	if opponent in ('Kansas City':
# 		opponent  = ('kan'
# 	if opponent in ('Minnesota':
# 		opponent  = ('min'
# 	if opponent in ('Chicago Sox':
# 		opponent  = ('chw'
# 	if opponent in ('Cleveland':
# 		opponent  = ('cle'
# 	if opponent in ('Detroit':
# 		opponent  = ('det'

# 	if opponent in ('New York Mets':
# 		opponent  = ('nym'
# 	if opponent in ('Atlanta':
# 		opponent  = ('atl'
# 	if opponent in ('Miami':
# 		opponent  = ('mia'
# 	if opponent in ('Washington':
# 		opponent  = ('was'
# 	if opponent in ('Philadelphia':
# 		opponent  = ('phi'

# 	if opponent in ('Chicago Cubs':
# 		opponent  = ('chc'
# 	if opponent in ('St. Louis':
# 		opponent  = ('stl'
# 	if opponent in ('Pittsburgh':
# 		opponent  = ('pit'
# 	if opponent in ('Milwaukee':
# 		opponent  = ('mil'
# 	if opponent in ('Cincinnati':
# 		opponent  = ('cin'

# 	if opponent in ('San Francisco':
# 		opponent  = ('sfo'
# 	if opponent in ('Los Angeles Dodgers':
# 		opponent  = ('lad'
# 	if opponent in ('Arizona':
# 		opponent  = ('ari'
# 	if opponent in ('San Diego':
# 		opponent  = ('sdg'
# 	if opponent in ('Colorado':
# 		opponent  = ('col'


print(pitcher_team)



# # Match pitcher names to RotoGuru

# 	if pitcher in ('Lance McCullers Jr.':
# 		pitcher = ('Lance McCullers'

# 	if pitcher in ('Vince Velasquez':
# 		pitcher = ('Vincent Velasquez'

# 	if pitcher in ('Mike Fiers':
# 		pitcher = ('Michael Fiers'

# 	if pitcher in ('J.A. Happ':
# 		pitcher = ('James Happ'

# 	if pitcher in ('JC Ramirez':
# 		pitcher = ('J.C. Ramirez'




