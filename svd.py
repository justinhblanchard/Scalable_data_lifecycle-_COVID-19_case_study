import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import TruncatedSVD
filename = sys.argv[1]
df = pd.read_csv(filename)
filename = filename[0:len(filename) - 3]
df1 = df.select_dtypes(include = 'object')
df = df.select_dtypes(exclude = 'object')
df = df.fillna(0)
print(df)
SVD = TruncatedSVD(n_components = 2)
df = SVD.fit_transform(df)
df = pd.DataFrame(df)
df.rename({0:SVD.explained_variance_ratio_[0], 1:SVD.explained_variance_ratio_[1]}, axis = 1, inplace = True)
df.reset_index(drop = True, inplace = True)
df1.reset_index(drop = True, inplace = True)
df1 = pd.concat([df1, df], axis = 1)
sns.scatterplot(data = df1, x = SVD.explained_variance_ratio_[0], y = SVD.explained_variance_ratio_[1], hue = 'location', alpha = 0.3)
plt.show()