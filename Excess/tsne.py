import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE
filename = sys.argv[1]
df = pd.read_csv('/Users/ihz/Desktop/Covid_Research/data/' + filename)
df = df.dropna()
df.drop_duplicates()
df1 = df.select_dtypes(include = 'object')
df = df.select_dtypes(exclude = 'object')
arr = df.to_numpy()
df = TSNE(n_components = 2, learning_rate = 'auto', init = 'random').fit_transform(arr)
df = pd.DataFrame(df)
df.rename({0:'tsne1', 1:'tsne2'}, axis = 1, inplace = True)
df1 = pd.concat([df1, df], axis = 1)
sns.scatterplot(data = df1, x = 'tsne1', y = 'tsne2', hue = 'location', alpha = 0.1)
plt.show()