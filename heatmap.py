import sys
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
filename = sys.argv[1]
df = pd.read_csv(filename)
corr1 = df.corr()
p2 = sns.heatmap(corr1, vmin = -1, vmax = 1, xticklabels = False, yticklabels = False, annot = True)
plt.savefig(filename + '_heatmap.png', bbox_inches = 'tight')