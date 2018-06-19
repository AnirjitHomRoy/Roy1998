Data$Age = ifelse(is.na(Data$Age), ave(Data$Age, 
FUN= function(x) mean(x, na.rm= TRUE)), Data$Age)


Data$Salary = ifelse(is.na(Data$Salary), ave(Data$Salary, 
              FUN= function(x) mean(x, na.rm= TRUE)), Data$Salary)
#x is the vector being operated upon
#is.na returns true if any value(s) is/are missing
#if the condition is satisfied, the operation preceding it is filled in 
#the desired column; otherwise the 3rd argument is filled in the working cell
rm(testing_set)
Data$Country = factor(Data$Country, 
                      levels= c('France', 'Spain', 'Germany'),
                      labels= c(1,2,3))
#levels->  a vector of the values x might have taken
Data$Purchased = factor(Data$Purchased, 
                      levels= c('Yes', 'No'),
                      labels= c(1,2))
#splitting the dataset into test and training sets
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
training_set[, 2:3] = scale(training_set[, 2:3])
test_set[, 2:3] = scale(test_set[, 2:3])


