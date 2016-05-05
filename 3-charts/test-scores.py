from os import path

import matplotlib.pyplot as plt
import pandas as pd

filename = path.join('matplotlibsampler', 'data', 'schools', 'sat-2014.csv')

fig, ax = plt.subplots()
df = pd.read_csv(filename)
df = df.convert_objects(convert_numeric=True)
ax.scatter(df['number_of_test_takers'], df['percent_scores_gte_1500'])
ax.set_xlim(0, 1000) # Remove some outliers for legibility

ax.set_title('High scores at a school vs Number of test takers there')
ax.set_ylabel('Percentage of Scores greater than or equal to 1500')
ax.set_xlabel('Number of test takers')

fig.savefig('scores.png')
