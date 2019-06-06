# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:57:15 2019

@author: MAHESH    ALLADI
"""

import pandas as pd
import numpy
import matplotlib.pyplot as plt
df=pd.read_excel(r"C:\Users\MAHESH ALLADI\.spyder-py3\mechine learning program\kmeans1.xlsx")
#print(df.head())
#print(df.corr())
#df.hist()
#plt.show()
#from pandas.plotting import scatter_matrix
#scatter_matrix(df)
#plt.show()
#fig=plt.figure()
#ax=fig.add_subplot(111)
#cax=ax.matshow(df.corr(),vmax=1,vmin=-1)
#plt.show()
df1=df.drop(["Model","Department"],axis=1)
#print(df1.head())
from sklearn.cluster import KMeans
model=KMeans(n_clusters=5)
#print(model)
model.fit(df1)
pr=model.predict(df1)
#print(pr)
df1["cluster"]=pr
#print(df1.head())
df2=df1.sort_values("cluster")
print(df2.head())
