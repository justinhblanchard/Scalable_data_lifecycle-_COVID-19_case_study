import sys
import pandas as pd
from sklearn.preprocessing import StandardScaler
filename = sys.argv[1]
df = pd.read_csv(filename)
filename = filename[0:len(filename) - 4]
scale = StandardScaler()
df_scaled = scale.fit_transform(df.select_dtypes(exclude = 'object'))
df1 = df.select_dtypes(include = 'object')
df_scaled = pd.DataFrame(df_scaled, columns = df.select_dtypes(exclude = 'object').columns)
df1 = pd.concat([df1, df_scaled], axis = 1)
df1.to_csv(filename + '_std.csv', index = False)