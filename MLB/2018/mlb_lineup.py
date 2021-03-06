import csv
import re
import unicodedata
import sys
import os



game_date = 20180620

####################    DO NOT CHANGE BELOW THIS LINE  ###########################


#path to file directory - HOME
# formats = ('/Users/Chris/Desktop/Statis/MLB/2018/formats/')


#path to file directory - WORK
downloads = '/Users/chrismccallan/Downloads'
formats = '/Users/chrismccallan/Downloads'


ifile  = os.path.join(downloads, 'dk_mlb_raw_lineups_%d.csv' % (game_date))
ofile  = os.path.join(formats, 'dk_mlb_lineup_comparison_upload_%d.csv' % (game_date))
ofile  = open(ofile, 'w')
writer = csv.writer(ofile)


with open(ifile, 'r') as csvfile:
	reader = csv.reader(csvfile)

	for row in reader:
		game_date         = game_date
		
		lineup_source     = re.sub(r'\s\(.*?\)\s\s\S\d{1,}', '', row[0])
		lineup_source     = re.sub(r'\s[A-Z]{3}/[A-Z]{3}/[A-Z]{3}\s\s\S\d{1,}', '', lineup_source)
		lineup_source     = re.sub(r'\s[A-Z]{3}\s\s\S\d{1,}', '', lineup_source)
		lineup_source     = re.sub(r'\s\s\S\d{1,}', '', lineup_source)
		
		lineup_rank       = re.sub(r'\s\(.*?\)', '', row[0])
		lineup_rank       = re.sub(r'Last 5 Games Avg Pitcher Adjusted\s\s\D', '', lineup_rank)
		lineup_rank       = re.sub(r'Last 5 Games Avg\s\s\D', '', lineup_rank)
		lineup_rank       = re.sub(r'DFS Guru NBA/MLB/NFL\s\s\D', '', lineup_rank)
		lineup_rank       = re.sub(r'RotoQL MLB\s\s\D', '', lineup_rank)
		lineup_rank       = re.sub(r'Perfect Lineup\s\s\D', '', lineup_rank)
		lineup_rank       = re.sub(r'Baseball Prospectus\s\s\D', '', lineup_rank)
		lineup_rank       = re.sub(r'Season Avg\s\s\D', '', lineup_rank)
		lineup_rank       = re.sub(r'Strategy 1\s\s\D', '', lineup_rank)
		lineup_rank       = re.sub(r'Strategy 2\s\s\D', '', lineup_rank)
		lineup_rank       = re.sub(r'Strategy 3\s\s\D', '', lineup_rank)
		lineup_rank       = re.sub(r'Strategy 4\s\s\D', '', lineup_rank)
		lineup_rank       = re.sub(r'Strategy 5\s\s\D', '', lineup_rank)
		lineup_rank       = re.sub(r'Strategy 6\s\s\D', '', lineup_rank)
		lineup_rank       = re.sub(r'Strategy 7\s\s\D', '', lineup_rank)
		lineup_rank       = re.sub(r'Strategy 8\s\s\D', '', lineup_rank)
		lineup_rank       = re.sub(r'filter_18_to_21_mix\s\s\D', '', lineup_rank)
		lineup_rank       = re.sub(r'filter_21\s\s\D', '', lineup_rank)
		
		
		pitcher_1         = re.sub(r'\s\(.*?\)', '', row[1])
		pitcher_2         = re.sub(r'\s\(.*?\)', '', row[2])
		catcher           = re.sub(r'\s\(.*?\)', '', row[3])
		first_base        = re.sub(r'\s\(.*?\)', '', row[4])
		second_base       = re.sub(r'\s\(.*?\)', '', row[5])
		third_base        = re.sub(r'\s\(.*?\)', '', row[6])
		short_stop        = re.sub(r'\s\(.*?\)', '', row[7])
		outfield_1        = re.sub(r'\s\(.*?\)', '', row[8])
		outfield_2        = re.sub(r'\s\(.*?\)', '', row[9])
		outfield_3        = re.sub(r'\s\(.*?\)', '', row[10])
		lineup_salary     = row[11]
	
		output = (game_date, lineup_source, lineup_rank, pitcher_1, pitcher_2, catcher, first_base, second_base, third_base, short_stop, outfield_1, outfield_2, outfield_3, lineup_salary)
		writer.writerows([output])