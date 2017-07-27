import csv #imports python csv module
import re  #imports python regular expressions library
import numpy as np
import pandas as pd

ifile  = 'mlb_gameday_raw.csv'
data = pd.read_csv(ifile, sep=',', encoding='ISO-8859-1', na_values='NaN') #RotoQL player csv export
df = pd.DataFrame(data)
df = df.iloc[:, [0,1,4]]

ofile  = 'dk_mlb_gameday_20170726.csv' #projection upload to BigQuery
df.to_csv(ofile, index=False)

# output = (game_date, pitcher, team, opponent)
# writer.writerows([d])

print(data)


# data.close()
# ofile.close()