# -*- coding: utf-8 -*-
"""
Created on Fri May 18 21:48:31 2018

@author: ANIRJIT
"""

import numpy as np
import matplotlib.pyplot as mt
import pandas as pd

#importing dataset
dataset= pd.read_csv('Data.csv')
x= dataset.iloc[:, :-1].values
y= dataset.iloc[:, 3].values
print(x)
np.set_printoptions(threshold=np.nan)  

#splitting the dataset into test and training sets
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.2, random_state= 0)
#fraction of the total size of observations occupied by test set

#feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)"""

