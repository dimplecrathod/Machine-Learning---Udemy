# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 20:42:49 2019

@author: EliteBook
"""

#Data preprocessing
#Importing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import os
#print(os.getcwd())

#Importing Dataset 
dataset = pd.read_csv('Data.csv')

#all columns except last column
X = dataset.iloc[:, :-1].values
#creating dependent variable
Y = dataset.iloc[:, 3].values

#Taking care of Missing Data
from sklearn.impute import SimpleImputer
#creating object of class
#axis = 0 (impute along columns)
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean', fill_value = None)
imputer = imputer.fit(X[:,1:3])

X[:,1:3] = imputer.transform(X[:, 1:3])

#Encoding Categorical Data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer, make_column_transformer
 #applying labelencoder to column one (country column)
labelEncoder_X = LabelEncoder()
X[:, 0] = labelEncoder_X.fit_transform(X[:, 0])
 #applying onehotencoder to column 0
columntransformer = make_column_transformer(
    (OneHotEncoder(categories='auto'), [0]),
    remainder='passthrough')
X = columntransformer.fit_transform(X)

#applying labelencoder to column 3
labelencoder_y = LabelEncoder()
Y =labelencoder_y.fit_transform(Y)

#Splitting the dataset into Training Set and Test Set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
