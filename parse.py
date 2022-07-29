import sys
import os
import wget
import pandas as pd
response = wget.download(sys.argv[1])
if response.endswith('.csv'):
    df = pd.read_csv(response)
else:
    df = pd.read_excel(response)
df = df.drop_duplicates()
df = df.dropna(how = 'all', axis = 1)
df1 = df.select_dtypes(include = 'object')
for i in df1.columns:
    if i != 'state' and i != 'State' and i != 'states' and i != 'States' and i != 'country' and i != 'Country' and i != 'countries' and i != 'Countries' and i != 'Jurisdiction of Occurrence':
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