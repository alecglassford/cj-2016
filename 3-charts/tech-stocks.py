from glob import glob
from os import path

import matplotlib.pyplot as plt
import pandas as pd

stocks_dir = path.join('matplotlibsampler', 'data', 'stocks', '*')

fig, ax = plt.subplots()
for filename in glob(stocks_dir):
    df = pd.read_csv(filename)
    df = df.reindex(index=df.index[::-1])
    ax.plot(df['Close'], label=path.basename(filename)[:-4])

# Assume dates are same on all of them :-o
indices = range(len(df) - 1, 0, - len(df)/5) # hack to deal with backward indices
ax.set_xticks([len(df) - index for index in indices])
ax.set_xticklabels(list(df.ix[indices]['Date']))

ax.legend()
ax.set_title('Stock prices at close of each day')
ax.set_ylabel('Price ($)')
ax.set_xlabel('Date')

fig.savefig('stocks.png')
