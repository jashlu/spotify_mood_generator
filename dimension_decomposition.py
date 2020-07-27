import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt


import pandas as pd


df = pd.read_csv('tracks.csv')                  #read tracks

features = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness',
              'liveness', 'valence']            #declare variables that we will set for "x"
            
x = df.loc[:, features].values

y = df.loc[:,['title']].values                  #make y the title variable of each song 


x = StandardScaler().fit_transform(x)           #standardize the data, by scaling the values
print(x)




## Now we can test multiple different dimensionality reduction techniques

#usinf PCA first
pca = PCA(n_components=2)
print(pca)

principalComponents = pca.fit_transform(x)

principalDf = pd.DataFrame(data = principalComponents
             , columns = ['component 1', 'component 2'])

print(principalDf)



