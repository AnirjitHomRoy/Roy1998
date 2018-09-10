import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing dataset
dataset= pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)   
#tab separated values
# quoting specifies which symbol to ignore
# dataset[column][index of the row]

#Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords    
# we are basically creating a corpus of all the available reviews
from nltk.stem.porter import PorterStemmer

corpus= []
for i in range(1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i]) 
    #input in the brackets---what not to remove 
    # ^ signifies what we don't want to remove
    review= review.lower()
    review= review.split()
    # In python the algorithms work faster with sets rather than lists
    ps =PorterStemmer()
    review= [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]# Stemming
    review= ' '.join(review)
    corpus.append(review)
    
# Creating a bag of workds model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features= 1500)  
    # Applying this object will convert the reviews to 
    # lowercase before creating the bag of words model
X= cv.fit_transform(corpus).toarray()
y= dataset.iloc[:, 1].values

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test) """
# not necessary because the outputs are small 

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

   