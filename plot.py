import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
filename = sys.argv[1]
df1 = pd.read_csv('/Users/ihz/Desktop/Covid_Research/data/' + filename)
df1.drop_duplicates()
x = (df1.iat[0, 0],)
for i in range (1, 9):
    x = x + (df1.iat[int(df1.index.size / 8 * i) - 1, 0],)
df1 = df1.select_dtypes(exclude = 'object')
for i in range(0, df1.columns.size):
    plt.plot(df1.iloc[:,i], label = df1.columns[i])
plt.xticks(np.linspace(0, df1.index.size, num = 9, endpoint = True), x, rotation = 20)
plt.legend()
plt.show()
plt.savefig('/Users/ihz/Desktop/Covid_Research/plots/' + filename + '_plot.png', bbox_inches = 'tight')