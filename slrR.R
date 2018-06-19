#Simple Linear Regression
#import the dataset

install.packages('caTools')
library(caTools)  #no quotes
set.seed(123)   #analogous to random_state in python
split=sample.split(Salary_Data$Salary, SplitRatio = 2/3)
#returns true or false
# only the dependent variable is to be entered, unlike python
# The split ratio corresponds to the training set
training_set = subset(Salary_Data, split == TRUE) #true signifies training set
test_set = subset(Salary_Data, split == FALSE) 

#feature scaling
# scale function is applicable only to numeric data 
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])


#fitting SLR to the training set
regressor= lm(formula = Salary ~ YearsExperience, data= training_set)
#"formula" expresses the dependent variable as a product of the dep. var.

#Predicting the test set results
y_pred= predict(regressor, newdata = test_set)


#Visualizing the training set results
ggplot()+
  geom_point(aes(x= training_set$YearsExperience, y= training_set$Salary),color= 'red')+
  geom_line(aes(x= training_set$YearsExperience, y= predict(regressor,newdata= training_set)), 
             color= 'blue')+
  ggtitle('Salary vs Experience(Training Set)')+
  xlab('Experience in years')+
  ylab('Salary')

#Test set results
ggplot()+
  geom_point(aes(x= test_set$YearsExperience, y= test_set$Salary),color= 'red')+
  geom_line(aes(x= training_set$YearsExperience, y= predict(regressor,newdata= training_set)), 
            color= 'blue')+           #the regressor is trained using training set so no change here
  ggtitle('Salary vs Experience(Test Set)')+
  xlab('Experience in years')+
  ylab('Salary')




