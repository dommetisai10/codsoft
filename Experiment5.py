import pandas as pd
import numpy as np
data=pd.read_csv(r"D:\Machine learning\ml.csv")
data=data.fillna(0)
x=data.iloc[ : , :-1].values
y=data.iloc[ : ,-1].values

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3,random_state=5)

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=3)

model.fit(xtrain,ytrain)
ypred=model.predict(xtest)
print(ypred)
#from sklearn.metrics import accuracy_score
#print(accuracy_score(ytest,ypred))
