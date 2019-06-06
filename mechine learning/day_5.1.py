#project number 1
import pandas
import numpy
import matplotlib.pyplot as plt
path=r"C:\Users\MAHESH ALLADI\.spyder-py3\mechine learning program\primeindiansdiabetes.csv"
names=["no.of tymes pregnant","plasme conct","bp","fold thickness","2hr ser insulin","body mass index","pedgree function","age","target"]
data=pandas.read_csv(path,names=names)

X=data.iloc[:,:8].values
y=data.iloc[:,8].values
#print(x)
#print(y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.33,random_state=5)
#print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=6)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
y_pred1=model.predict(numpy.array([[200,134,234,22,456,234,54,12]]))
print(y_pred1)
#print(y_pred.shape)
from sklearn.metrics import confusion_matrix
print("confusion matrics:",confusion_matrix(y_test,y_pred))
from sklearn.metrics import accuracy_score
print("accuracy:",accuracy_score(y_test,y_pred)*100)
data.hist()
plt.show()
