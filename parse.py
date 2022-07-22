import sys
import pandas as pd
filename = sys.argv[1]
df = pd.read_csv('/Users/ihz/Desktop/Covid_Research/data/' + filename)
df = df.dropna()
df = df.drop_duplicates()
df.to_csv('/Users/ihz/Desktop/Covid_Research/data/parsed.csv', index = False)