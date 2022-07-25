import sys
import pandas as pd
df = pd.read_csv(sys.argv[1])
df = df.drop_duplicates()
df = df.dropna(how = 'all', axis = 1)
df1 = df.select_dtypes(include = 'object')
for i in df1.columns:
    if i != 'dates' and i != 'Dates' and i != 'date' and i != 'Date' and i != 'state' and i != 'State' and i != 'states' and i != 'States' and i != 'country' and i != 'Country' and i != 'countries' and i != 'Countries':
        df1 = df1.drop(i, axis = 1)
df = df.select_dtypes(exclude = 'object')
df = pd.concat([df1, df], axis = 1)
df.to_csv('parsed.csv', index = False)
name = 1
for i in df.iloc[:, 1].unique():
    df.loc[(df.iloc[:, 1] == i)].to_csv(i + '.csv', index = False)
    name += 1
