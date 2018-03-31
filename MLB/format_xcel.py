import pandas as pd
import numpy as np

ifile = 'workbook.xlsx'
ofile  = 'dk_mlb_gameday_20170728.csv' #gameday data upload to BigQuery


# Load spreadsheet from ESPN MLB Schedule 

mlb_gameday = pd.ExcelFile(ifile, encoding='ISO-8859-1')


# Parse spreadsheet to include only the columns for team, opponent, and pitchers
data = mlb_gameday.parse(0, parse_cols=[0,1,4], header=None, na_values='NaN', names=['Team', 'Opponent', 'Pitching Matchup'], dtype=str)


# Create a Pandas DataFrame from the spreadsheet 'data'
df_alpha = pd.DataFrame(data)


#Split the Pitching Matchup column of the 'df_alpha' DataFrame and name the new columns
matchup_split = df_alpha['Pitching Matchup'].apply(lambda x: pd.Series(x.split('vs')))
matchup_split.columns = ['Team Pitcher', 'Opponent Pitcher']


# Combine the columns from the df_alpha DataFrame with the newly created columns from 'matchup_split'
df_beta = pd.concat([df_alpha, matchup_split], axis=1)


# Define the data to be included in the final DataFrame (omits Pitching Matchup)
df = df_beta.iloc[:, [0,1,3,4]]


# Remove empty rows from the df DataFrame
for team in df['Team']:
	df['Team'].replace('', np.nan, inplace=True)

for opponent in df['Opponent']:
	df['Opponent'].replace('', np.nan, inplace=True)

for pitcher in df['Team Pitcher']:
	df['Team Pitcher'].replace('', np.nan, inplace=True)

for pitcher in df['Opponent Pitcher']:
	df['Opponent Pitcher'].replace('', np.nan, inplace=True)

df.dropna(subset=['Team','Opponent','Team Pitcher', 'Opponent Pitcher'], inplace=True)



df.to_csv(ofile, index=False)
print(df)
