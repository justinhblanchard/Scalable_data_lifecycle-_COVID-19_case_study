import sys
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
filename = sys.argv[1]
df = pd.read_csv(filename)
p1 = sns.pairplot(df, kind = 'reg', diag_kind = 'kde', plot_kws={'line_kws':{'color':'red'}, 'scatter_kws': {'alpha': 0.1}})
plt.savefig(filename + '_point.png', bbox_inches = 'tight')