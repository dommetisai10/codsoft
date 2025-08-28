import pandas as pd
import numpy as np

from sklearn.datasets import load_iris
data=load_iris()
x=data.data
y=data.target

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3,random_state=5)

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()

model.fit(xtrain,ytrain)
ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score
print(accuracy_score(ypred,ytest))

