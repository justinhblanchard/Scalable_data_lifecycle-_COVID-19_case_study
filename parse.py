import sys
import os
import wget
import pandas as pd
#downloads the file
response = wget.download(sys.argv[1])
#reads the file
if response.endswith('.csv'):
    df = pd.read_csv(response)
else:
    df = pd.read_excel(response)
#preprocessing
df = df.drop_duplicates()
df = df.dropna(how = 'all', axis = 1)
df = df.drop('MMWR Year', axis=1)
df = df.drop('MMWR Week', axis=1)
df1 = df.select_dtypes(include = 'object')
for i in df1.columns:
    #filtering by a column name
    if i != 'Jurisdiction of Occurrence':
        df1 = df1.drop(i, axis = 1)
df = df.select_dtypes(exclude = 'object')
df = pd.concat([df1, df], axis = 1)
df = df.rename(columns = {df.columns[0]: 'location'})
os.mkdir('Parsed')
df.to_csv('Parsed/parsed.csv', index = False)
name = 1
for i in df.iloc[:, 0].unique():
    df.loc[(df.iloc[:, 0] == i)].to_csv('Parsed/' + i + '.csv', index = False)
    name += 1