#Simple Linear Regression

# Importing the dataset
dataset = read.csv('Salary_Data.csv')

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)

#Fitting Simple Linear Regression to Training Set
#lm is used to fit linear models
#formula = Salary ~ YearsExperience (Salary is dependent on YearsExperience)
regressor =lm( formula = Salary ~ YearsExperience , data = training_set)

#type summary(regressor) in console to get standard error, r squared value etc after implementing above step
#the P-value is another indicator of the statistical significance because the lower the p value is the more significant your independent variable is going
# to be. That is the more impact the more effect your independent variable is going to have on the dependent variable.
#And usually a good threshold for the P-value is five percent which means that when you are below 5 percent the independent variable is highly significant.
#And when we are over 5 percent that means that it's less significant.

#Predicting the Test Set Results
Y_Pred = predict(regressor, newdata = test_set)

#Visualising the Training Set Results
#install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x= training_set$YearsExperience, y = training_set$Salary), colour = 'red') +
  geom_line(aes( x = training_set$YearsExperience, y = predict( regressor, newdata = training_set)), colour = 'blue') +
  ggtitle('Salary vs Experience (Train Set)') +
  xlab('Years of Experience') +
  ylab('Salary')

#Visualising the Test Set Results
#install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x= test_set$YearsExperience, y = test_set$Salary), colour = 'red') +
  geom_line(aes( x = training_set$YearsExperience, y = predict( regressor, newdata = training_set)), colour = 'blue') +
  ggtitle('Salary vs Experience (Test Set)') +
  xlab('Years of Experience') +
  ylab('Salary')