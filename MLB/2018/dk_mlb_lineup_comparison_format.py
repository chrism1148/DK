import csv
import re
import unicodedata
import sys
import os



####################    DO NOT CHANGE BELOW THIS LINE  ###########################

game_date = 20180410

downloads = '/Users/chrismccallan/Downloads'
# formats = ('/Users/Chris/Desktop/Statis/MLB/2018/formats/')
formats = ('/Users/chrismccallan/Downloads')
regex = re.compile(".*?\((0-9)\)")


ifile  = os.path.join(downloads, 'csv1.csv')
ofile  = os.path.join(formats, 'dk_mlb_lineup_comparision_upload_%d.csv' % (game_date))
ofile  = open(ofile, 'w')
writer = csv.writer(ofile)


with open(ifile, 'r') as csvfile:
	reader = csv.reader(csvfile)
	# next(reader)

	for row in reader:
		game_date         = row[0]
		lineup_source     = re.sub(r'\s\(.*?\)\s\s\S\d{1,}', '', row[1])
		lineup_source     = re.sub(r'\s[A-Z]{3}/[A-Z]{3}/[A-Z]{3}\s\s\S\d{1,}', '', lineup_source)
		lineup_source     = re.sub(r'\s[A-Z]{3}\s\s\S\d{1,}', '', lineup_source)
		pitcher_1         = re.sub(r'\s\(.*?\)', '', row[2])
		pitcher_2         = re.sub(r'\s\(.*?\)', '', row[3])
		catcher           = re.sub(r'\s\(.*?\)', '', row[4])
		first_base        = re.sub(r'\s\(.*?\)', '', row[5])
		second_base       = re.sub(r'\s\(.*?\)', '', row[6])
		third_base        = re.sub(r'\s\(.*?\)', '', row[7])
		short_stop        = re.sub(r'\s\(.*?\)', '', row[8])
		outfield_1        = re.sub(r'\s\(.*?\)', '', row[9])
		outfield_2        = re.sub(r'\s\(.*?\)', '', row[10])
		outfield_3        = re.sub(r'\s\(.*?\)', '', row[11])
		lineup_salary     = row[12]
	

		output = (game_date, lineup_source, pitcher_1, pitcher_2, catcher, first_base, second_base, third_base, short_stop, outfield_1, outfield_2, outfield_3, lineup_salary)
		writer.writerows([output])

