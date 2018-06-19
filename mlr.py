# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 11:52:08 2018

@author: ANIRJIT
"""

#Multiple linear regression

import numpy as np
import matplotlib.pyplot as mt
import pandas as pd

#importing dataset
dataset= pd.read_csv('50_Startups.csv')
x= dataset.iloc[:, :-1].values
y= dataset.iloc[:, 4].values
print(x)
np.set_printoptions(threshold=np.nan)  

#encode categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()#creating an object of the class LabelEncoder
x[:, 3]= labelencoder_x.fit_transform(x[:, 3]) 
onehotencoder= OneHotEncoder(categorical_features= [3])#specifying the column(s) to
#be treated as categorical
x = onehotencoder.fit_transform(x).toarray()
#to.array() is required only for dummy encoding
#no need to specify column as it has been done prior to this

#Avoiding dummy variable trap------x= x[:, 1:]
#Don't need to do in Python

#splitting the dataset into test and training sets
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.2, random_state= 0)
#fraction of the total size of observations occupied by test set

#Fitting Multiple Linear Regression 
from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(x_train, y_train)

#Predicting the test results
y_pred= regressor.predict(x_test)


