import unicodedata
import csv

ifile  = open('dk_mlb_perfect_game_20180331.csv', 'r') #RotoQL player csv export
reader = csv.reader(ifile, delimiter=',')
ofile  = open('test.csv', 'w') #projection upload to BigQuery
writer = csv.writer(ofile)


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

for row in reader:
	players = remove_accents(row[7])

	print(players)