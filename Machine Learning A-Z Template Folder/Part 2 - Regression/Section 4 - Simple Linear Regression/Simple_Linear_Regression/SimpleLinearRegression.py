# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 19:24:47 2019

@author: EliteBook
"""

#Simple Linear Regression

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)


#We do not need to apply feature scaling for simple linear regression
# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

#Fitting Simple Linear Regression To Training Set
from sklearn.linear_model import LinearRegression
#creating object of LinearRegression class
regressor = LinearRegression() 
#fitting training set to regressor
regressor.fit(X_train, Y_train)


#predicting test results
Y_Pred = regressor.predict(X_test)
#compare values of Y_pred (model predicted values) and Y_test(actual values)

#Visualising Training Set Results
plt.scatter(X_train, Y_train, color= 'red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs. Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#Visualising Test Set Results
plt.scatter(X_test, Y_test, color= 'red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs. Experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


#model is making some very good predictions those new employees salaries most of the salaries lie on the best fitting line or are close to the best fitting line
