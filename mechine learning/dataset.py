# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

import pandas as pd
import matplotlib.pyplot as plt
ftr=["clg ranks","trndig %","pg fclty","clg infra %","ocpny strngth%","fee"]
d={}
for i in range(0,len(ftr)):
    if ftr[i]=="clg ranks":
        d1={ftr[i]:np.array(np.random.randint(1,4,18))}
        d.update(d1)
    elif ftr[i]=="fee":
        d1={ftr[i]:np.array(np.random.randint(20000,100000,18))}
        d.update(d1)
    else:
        d1={ftr[i]:np.array(np.random.randint(1,100,18))}
        d.update(d1)
#print(d)
li=[]
for i in range(2001,2019):
    li.append(str(i)) 
#print(li)
##a=np.arange(2001,2019)
##print(a)
df = pd.DataFrame(d,index=li)


print(df)
#corrl=df.corr()
#print(corrl)
#print(df.describe())
#print(df.head())
#print(df.tail())
#correlations=df.corr()
#print(correlations)
#fig=plt.figure()
#ax=fig.add_subplot(111)
#cax=ax.matshow(correlations,vmax=1,vmin=-1)
#fig.colorbar(cax)
#ticks=np.arange(0,len(ftr),1)
#ax.set_xticks(ticks)
#ax.set_yticks(ticks)
#ax.set_xticklabels(ftr)
#ax.set_yticklabels(ftr)
#plt.show()
#from pandas.plotting import scatter_matrix
#scatter_matrix(df)
#plt.show()




