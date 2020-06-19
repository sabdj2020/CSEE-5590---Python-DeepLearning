# libraries
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

# glass data set with pd.read_csv in pandas Library
data = pd.read_csv('DataSet/glass.csv')

# select columns predictors in data set
x = data[['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']]

# select the target - Type -
y = data['Type']

# Use train_test_split to create training and testing part
# Train/Test split
# 1- Split the dataset into two sets
# 2- Train the model on the Training set
# 3- Test the model on the Testing Set, and evaluate how well we did

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# print the train and test shape
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)
# create a naive bayes model using GaussianNB()
model = GaussianNB()
# train the model using fit() method
model.fit(X_train, y_train)
# print the model accuracy
print('Naive Bayes accuracy on training set: {:.2f}'.format(model.score(X_train, y_train)))
print('Naive Bayes accuracy on test set: {:.2f}'.format(model.score(X_test, y_test)))