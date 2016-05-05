from os import path

import matplotlib.pyplot as plt
import pandas as pd

legislators_filename = path.join('matplotlibsampler', 'data', 'congress', 'legislators.csv')
tweets_filename = path.join('matplotlibsampler', 'data', 'congress', 'legislators-twitter.csv')
categories = ['Tweets', 'Favorites', 'Following', 'Followers', 'Listed']
ticks = list(range(len(categories)))

fig, ax = plt.subplots()
legislators = pd.read_csv(legislators_filename)
tweets = pd.read_csv(tweets_filename)
df = pd.merge(legislators, tweets, left_on='twitter_id', right_on='Screen name')
democrats = df[df['party'] == 'D']
republicans = df[df['party'] == 'R']
democrat_vals = [democrats[cat].median() for cat in categories]
republican_vals = [republicans[cat].median() for cat in categories]
ax.bar(ticks, democrat_vals, align='center', label='Democrats', color='blue')
ax.bar(ticks, republican_vals, align='center', bottom=democrat_vals,
       label='Republicans', color='red')
ax.set_xticks(ticks)
ax.set_xticklabels(categories)

ax.legend()
ax.set_title('Twitter metrics for legislators')
ax.set_ylabel('Median count among all legislators')

fig.savefig('congress_twitter.png')
