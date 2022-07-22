import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
filename = sys.argv[1]
df = pd.read_csv('/Users/ihz/Desktop/Covid_Research/data/' + filename)
df = df.dropna()
df = df.drop_duplicates()
df1 = df.select_dtypes(include = 'object')
df = df.select_dtypes(exclude = 'object')
cov = np.cov(df, rowvar = False)
vals , vecs = np.linalg.eigh(cov)
index = np.argsort(vals)[::-1]
svals = vals[index]
svecs = vecs[:, index]
valsum = sum(vals)
