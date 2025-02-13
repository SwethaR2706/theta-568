from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')
df=pd.read_csv('Universities.csv')
df.head()
plt.scatter(df.SAT,df['Top10'])
plt.xlabel('SAT')
plt.ylabel('Top10')
from sklearn.cluster import KMeans
km=KMeans(n_clusters=3)
y_predicted=km.fit_predict(df[['Expenses','GradRate']])
y_predicted
df['Cluster']=y_predicted
km.cluster_centers_
df1=df[df.Cluster==0]
df2=df[df.Cluster==1]
df3=df[df.Cluster==2]
plt.scatter(df1.Top10,df1['SFRatio'],color='green')
plt.scatter(df2.Top10,df2['SFRatio'],color='red')
plt.scatter(df3.Top10,df3['SFRatio'],color='black')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.xlabel('Top10')
plt.ylabel('SFRatio')
plt.legend()
