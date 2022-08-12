import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
filename = sys.argv[1]
filename = sys.argv[1]
df = pd.read_csv(filename)
filename = filename[0:len(filename) - 3]
df1 = df.select_dtypes(include = 'object')
df = df.select_dtypes(exclude = 'object')
pca = PCA(n_components = 2)
df = pca.fit_transform(df)
df = pd.DataFrame(df)
vals = np.arange(pca.n_components_) + 1
plt.plot(vals, pca.explained_variance_ratio_, 'o-')
plt.title('Scree Plot')
plt.xlabel('Principal Component')
plt.ylabel('Variance Explained')
plt.savefig(filename + '_scree.png', bbox_inches = 'tight')
df.rename({0:'pca1', 1:'pca2'}, axis = 1, inplace = True)
df.reset_index(drop = True, inplace = True)
df1.reset_index(drop = True, inplace = True)
df1 = pd.concat([df1, df], axis = 1)
df1.to_csv(filename, index = False)