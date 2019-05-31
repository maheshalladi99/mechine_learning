import numpy
import pandas
import sklearn
import matplotlib
'''a=[[2,3,4,5],[6,7,8,9]]
a1=numpy.array(a)
print(a1)
a2=numpy.shape(a)
print(a2)
print(a1[0])
print(a1[-1])
print(a1[:,3])
a3=numpy.arange(3,16)
print(a3)

a3=numpy.arange(3,16,2)
print(a3)
a3=numpy.arange(3,16,-1)
print(a3)
a3=numpy.arange(3,16,2.1)
print(a3)
a3=numpy.arange(30,-1,-15)
print(a3)
a3=numpy.zeros(16)
print(a3)
a3=numpy.zeros((3,3))
print(a3)
a3=numpy.zeros((16,5))
print(a3)
a3=numpy.ones(16)
print(a3)
a3=numpy.zeros((16,3))
print(a3)
a3=numpy.ones((5,5))
print(a3*5)
a3=numpy.eye(3)
print(a3)
a3=numpy.random.rand(2,3)
print(a3)
a3=numpy.random.randint(2,100,4)
print(a3)
print(a3.shape)

a3=numpy.random.randint(2,100,(5,5))
print(a3)
a3=numpy.random.randint(2,10,20)
print(a3)

a3=np.random.randint(2,100,(5,5))
print(a3)
import numpy as np
from numpy.random import randint as ri
a3=ri(2,100,30)
#print(a3)
b=a3.reshape(2,3,5)
#print(b)
b=a3.reshape(6,5)
print(b)
print(b[ : , -1])
print(b[0])
a=ri(1,200,20)
#print(a)
#
a=ri(1,200,20).reshape(5,4)
#print(a)
#print(np.sort(a))
#print(np.sort(a,axis=0))
#print(a[3:5,2:4])'''
#about pandas
label=['a','b','c']
data1=[10,20,30]
arr=numpy.array(label)
#print(arr)
s1=pandas.Series(data=data1,index=label)
print(s1)
print(s1[0])
print(s1["a"])
s1=pandas.Series([1,2,3,4,5,6],['a','b','c','d','e','f'])
print(s1)
print(s1[::-1])
s2=pandas.Series([1,2,3,4,5,6],['b','a','c','d','e','f'])
print(s1+s2)




















