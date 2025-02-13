from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
file_path = "/content/Wholesale customers data.csv"
df = pd.read_csv(file_path)
df
print(df.info())
df.drop(['Channel','Region'],axis=1,inplace=True)
c
array
stscaler=StandardScaler().fit(array)
X=stscaler.transform(array)
X
dbscan=DBSCAN(eps=0.8,min_samples=6)
dbscan.fit(X)
dbscan.labels_
c1=pd.DataFrame(dbscan.labels_,columns=['cluster'])
c1
pd.concat([df,c1],axis=1)
