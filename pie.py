import sys
import pandas as pd
import matplotlib.pyplot as plt
filename = sys.argv[1]
df = pd.read_csv('/Users/ihz/Desktop/Covid_Research/data/' + filename, index_col = 0)
df.drop_duplicates()
for i in df.select_dtypes(exclude = object).columns:
    df.plot(kind = 'pie', labels = None, y = i, autopct = '%1.0f%%')
    plt.legend(labels = df.index)
    plt.plot()
    plt.savefig('/Users/ihz/Desktop/Covid_Research/plots/' + i + '_pie.png', bbox_inches = 'tight')