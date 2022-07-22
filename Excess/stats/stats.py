import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/ihz/Desktop/Covid_Research/stats/heatmap.csv', index_col = 0)
print(df)
p1 = sns.heatmap(df, vmin = -1, vmax = 1, annot = True)
plt.show()