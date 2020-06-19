# libraries to import
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

# load glass data set
data = pd.read_csv('DataSet/glass.csv')

# select the column
x = data[['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']]

# select the target column which is type
y = data['Type']

# Use train_test_split to create training and testing part
# split the dataset  70% (0.3) for training, 30% for testing
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# print the train and test shape
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

# create svm using LinearSVC()
svm = LinearSVC(random_state=0, tol=1e-5)

# train the model using fit() method
svm.fit(X_train, y_train)

# print the model accuracy
print('SVM classifier accuracy on training SET: {:.2f}'.format(svm.score(X_train, y_train)))
print('SVM classifier accuracy on test SET: {:.2f}'.format(svm.score(X_test, y_test)))