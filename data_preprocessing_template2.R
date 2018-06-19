#import the dataset
data= data[]
#install.packages('caTools')
library(caTools)  #no quotes
set.seed(123)   #analogous to random_state in python
split=sample.split(Data$Purchased, SplitRatio = 0.8)#returns true or false
# only the dependent variable is to be entered, unlike python
# The split ratio corresponds to the training set
training_set = subset(Data, split == TRUE) #true signifies training set
test_set = subset(Data, split == FALSE) 

#feature scaling
# scale function is applicable only to numeric data 
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])
