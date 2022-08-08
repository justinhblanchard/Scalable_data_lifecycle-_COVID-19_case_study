import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
filename = sys.argv[1]
df = pd.read_csv('/Users/ihz/Desktop/Covid_Research/data/' + filename)
df = df.dropna()
df = df.drop_duplicates()
df1 = df.select_dtypes(include = 'object')
df = df.select_dtypes(exclude = 'object')
kmeans = KMeans(n_clusters = 4, random_state = 0).fit(df)
sns.scatterplot(data = df, x = df.columns[0], y = df.columns[1], hue = kmeans.labels_ + 1, alpha = 0.6)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], marker= "X", label = "centroids")
plt.legend()
plt.show()