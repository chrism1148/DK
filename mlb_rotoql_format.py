import csv #imports python csv module
import re  #imports python regular expressions library

ifile  = open('mlb_rotoql.csv', 'r', encoding='ISO-8859-1',) #RotoQL player csv export
reader = csv.reader(ifile, delimiter=',')
ofile  = open('mlb_rotoql_20170519.csv', 'w') #projection upload to BigQuery
writer = csv.writer(ofile)

# define fields from RotoGuru MLB CSV

for row in reader:
	player_id   = row[0].strip()
	player      = row[2].strip()
	dk_position = row[7].strip()
	team        = row[8].lower()


# Match RotoQL team abbreviations to RotoGuru abbreviations

	if team in ('cws'):
		team      = ('chw')
	if team in ('kc'):
		team      = ('kan')
	if team in ('wsh'):
		team      = ('was')
	if team in ('sf'):
		team      = ('sfo')
	if team in ('sd'):
		team      = ('sdg')

	if team in ('tb'):
		team      = ('tam')

	output = (player_id, player, team, dk_position)
	writer.writerows([output])

ifile.close()
ofile.close()