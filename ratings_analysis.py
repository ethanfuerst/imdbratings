#%%
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

#%%
with open('ratings.csv', 'r', encoding='mac_roman', newline='') as csvfile:
    df = pd.read_csv(csvfile)

def media_kind(x):
    if x == 'movie':
        return 'Movie'
    elif x == 'tvSeries':
        return 'TV'

df['Release Date'] = pd.to_datetime(df['Release Date'])
df['Date Rated'] = pd.to_datetime(df['Date Rated'])
# Get number of days
df['Days waited to see'] = df['Date Rated'] - df['Release Date']
df['Days waited to see'] = (df['Days waited to see'].astype(int) / int(float('8.64e+13'))).astype(int)

df['Title Type'] = df['Title Type'].apply(media_kind)

df.to_csv('ratings_clean.csv', index=False)
# %%
plt.scatter(df['IMDb Rating'], df['Your Rating'])
plt.title('IMDb Rating vs. My Rating')
plt.xlabel('IMDb Rating')
plt.ylabel('My Rating')
plt.show()

# %%
