import numpy as np
#from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt


from sklearn.cluster import AffinityPropagation


import pandas as pd


df = pd.read_csv('tracks.csv')                  #read tracks

print(df.describe())


features = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness',
              'liveness', 'valence']            #declare variables that we will set for "x"
            
#x = df.loc[:, features].values                  #x represents the features
                                                #features are individual independent variables that act as the 
                                                #input in system. 


'''
y = df.loc[:,['title']].values                  #y is the target
                                                #target is whatever the output of the input variables
                                                #it could be what the input variables are mapped to in classification
                                    
'''

# we need to standardize loudness, to 0-1 scale like rest of data, by using MinMaxScaler
loudness = df[['loudness']].values
standard_loudness = MinMaxScaler().fit_transform(loudness)
df['loudness'] = pd.DataFrame(standard_loudness)         #reassign loudness column



print(df.describe())

x = df.loc[:, features].values                  #x represents the features
                                                #features are individual independent variables that act as the 
                                                #input in system.


af = AffinityPropagation(preference=-50)
clustering = af.fit(x)

print(plt.scatter(x[:,0], x[:,1], c=clustering.labels_, cmap='rainbow', alpha=0.7, edgecolors='b'))

'''


## Now we can test multiple different dimensionality reduction techniques

#using PCA first
pca = PCA(n_components=2)
print(pca)

principalComponents = pca.fit_transform(x)

principalDf = pd.DataFrame(data = principalComponents
             , columns = ['component 1', 'component 2'])

print(principalDf)



'''
