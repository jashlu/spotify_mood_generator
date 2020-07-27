import numpy as np
from sklearn.decomposition import PCA

import pandas as pd


df = pd.read_csv('tracks.csv')
print(df)

features = ['title','danceability', 'energy', 'loudness', 'speechiness', 'acousticness',
              'liveness', 'valence']

x = df.loc['danceability', 'energy', 'loudness', 'speechiness', 'acousticness',
              'liveness', 'valence']
print(x)
y = df.loc[:,['title']].values
print(y)
