import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
df = pd.read_csv('/Users/ihz/Desktop/Covid_Research/data/parsed')
df1 = df.select_dtypes(include = 'object')
df = df.select_dtypes(exclude = 'object')
pca = PCA(n_components = 2)
df = pca.fit_transform(df)
df = pd.DataFrame(df)
df.rename({0:pca.explained_variance_ratio_[0], 1:pca.explained_variance_ratio_[1]}, axis = 1, inplace = True)
df.reset_index(drop = True, inplace = True)
df1.reset_index(drop = True, inplace = True)
df1 = pd.concat([df1, df], axis = 1)
vals = np.arange(pca.n_components_) + 1
df1.to_csv('/Users/ihz/Desktop/Covid_Research/data/pca.csv', index = False)
sns.scatterplot(data = df1, x = pca.explained_variance_ratio_[0], y = pca.explained_variance_ratio_[1], hue = 'location', alpha = 0.3)
c = np.transpose(pca.components_[0:2, :])
for i in range(c.shape[0]):
    plt.arrow(0, 0, c[i, 0] * 3, c[i, 1] * 3)
    plt.text(c[i,0] * 3.1, c[i,1] * 3.1, i + 1, alpha = 0.5)
plt.grid()
plt.savefig('/Users/ihz/Desktop/Covid_Research/plots/pca.png', bbox_inches = 'tight')