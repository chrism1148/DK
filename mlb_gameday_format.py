import csv #imports python csv module
import re  #imports python regular expressions library

ifile  = open('mlb_gameday_raw.csv', 'r', encoding='ISO-8859-1',) #RotoQL player csv export
reader = csv.reader(ifile, delimiter=',')
ofile  = open('dk_mlb_gameday_20170519.csv', 'w') #projection upload to BigQuery
writer = csv.writer(ofile)

# define fields from RotoGuru MLB CSV

date = '20170519'

for row in reader:
	game_date  = date
	pitcher    = row[0].strip()
	team       = row[1].strip()
	opponent   = row[2].strip()


# Match pitcher names to RotoGuru

	if pitcher in ('Lance McCullers Jr.'):
		pitcher = ('Lance McCullers')

	if pitcher in ('Vince Velasquez'):
		pitcher = ('Vincent Velasquez')

	if pitcher in ('Mike Fiers'):
		pitcher = ('Michael Fiers')





# Change teams to abbreviations

	if team in ('New York Yankees'):
		team      = ('nyy')
	if team in ('Boston'):
		team      = ('bos')
	if team in ('Baltimore'):
		team      = ('bal')
	if team in ('Tampa Bay'):
		team      = ('tam')
	if team in ('Toronto'):
		team      = ('tor')

	if team in ('Texas'):
		team      = ('tex')
	if team in ('Los Angeles Angels'):
		team      = ('laa')
	if team in ('Houston'):
		team      = ('hou')
	if team in ('Oakland'):
		team      = ('oak')
	if team in ('Seattle'):
		team      = ('sea')

	if team in ('Kansas City'):
		team      = ('kan')
	if team in ('Minnesota'):
		team      = ('min')
	if team in ('Chicago Sox'):
		team      = ('chw')
	if team in ('Cleveland'):
		team      = ('cle')
	if team in ('Detroit'):
		team      = ('det')

	if team in ('New York Mets'):
		team      = ('nym')
	if team in ('Atlanta'):
		team      = ('atl')
	if team in ('Miami'):
		team      = ('mia')
	if team in ('Washington'):
		team      = ('was')
	if team in ('Philadelphia'):
		team      = ('phi')

	if team in ('Chicago Cubs'):
		team      = ('chc')
	if team in ('St. Louis'):
		team      = ('stl')
	if team in ('Pittsburgh'):
		team      = ('pit')
	if team in ('Milwaukee'):
		team      = ('mil')
	if team in ('Cincinnati'):
		team      = ('cin')

	if team in ('San Francisco'):
		team      = ('sfo')
	if team in ('Los Angeles Dodgers'):
		team      = ('lad')
	if team in ('Arizona'):
		team      = ('ari')
	if team in ('San Diego'):
		team      = ('sdg')
	if team in ('Colorado'):
		team      = ('col')

	if opponent in ('New York Yankees'):
		opponent  = ('nyy')
	if opponent in ('Boston'):
		opponent  = ('bos')
	if opponent in ('Baltimore'):
		opponent  = ('bal')
	if opponent in ('Tampa Bay'):
		opponent  = ('tam')
	if opponent in ('Toronto'):
		opponent  = ('tor')

	if opponent in ('Texas'):
		opponent  = ('tex')
	if opponent in ('Los Angeles Angels'):
		opponent  = ('laa')
	if opponent in ('Houston'):
		opponent  = ('hou')
	if opponent in ('Oakland'):
		opponent  = ('oak')
	if opponent in ('Seattle'):
		opponent  = ('sea')

	if opponent in ('Kansas City'):
		opponent  = ('kan')
	if opponent in ('Minnesota'):
		opponent  = ('min')
	if opponent in ('Chicago Sox'):
		opponent  = ('chw')
	if opponent in ('Cleveland'):
		opponent  = ('cle')
	if opponent in ('Detroit'):
		opponent  = ('det')

	if opponent in ('New York Mets'):
		opponent  = ('nym')
	if opponent in ('Atlanta'):
		opponent  = ('atl')
	if opponent in ('Miami'):
		opponent  = ('mia')
	if opponent in ('Washington'):
		opponent  = ('was')
	if opponent in ('Philadelphia'):
		opponent  = ('phi')

	if opponent in ('Chicago Cubs'):
		opponent  = ('chc')
	if opponent in ('St. Louis'):
		opponent  = ('stl')
	if opponent in ('Pittsburgh'):
		opponent  = ('pit')
	if opponent in ('Milwaukee'):
		opponent  = ('mil')
	if opponent in ('Cincinnati'):
		opponent  = ('cin')

	if opponent in ('San Francisco'):
		opponent  = ('sfo')
	if opponent in ('Los Angeles Dodgers'):
		opponent  = ('lad')
	if opponent in ('Arizona'):
		opponent  = ('ari')
	if opponent in ('San Diego'):
		opponent  = ('sdg')
	if opponent in ('Colorado'):
		opponent  = ('col')



	output = (game_date, pitcher, team, opponent)
	writer.writerows([output])

ifile.close()
ofile.close()