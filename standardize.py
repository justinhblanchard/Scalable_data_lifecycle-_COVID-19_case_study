import sys
import pandas as pd
from sklearn.preprocessing import StandardScaler
df = pd.read_csv(sys.argv[1])
scale = StandardScaler()
df_scaled = scale.fit_transform(df.select_dtypes(exclude = 'object'))
df1 = df.select_dtypes(include = 'object')
df_scaled = pd.DataFrame(df_scaled, columns = df.select_dtypes(exclude = 'object').columns)
df1 = pd.concat([df1, df_scaled], axis = 1)
df1.to_csv('standardized_' + sys.argv[1], index = False)
