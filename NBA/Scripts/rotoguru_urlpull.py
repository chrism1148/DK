from urllib.request import urlretrieve
import pandas as pd

url = 'http://rotoguru1.com/cgi-bin/nba-dhd-2018.pl'

urlretrieve(url, 'nba_2017_season_test.csv')

df = pd.read_csv('nba_2017_season_test.csv', sep=':')

df.to_csv('nba_2017_season_formatted.csv')