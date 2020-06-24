# import libraries

import pandas as pd
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn import linear_model

# step1: acquire the data and create our environment
# read dataset
dataset = pd.read_csv('dataset/winequality-red.csv')
print("the 10th record\n", dataset.head(10))


# include numeric features
num_feat = dataset.select_dtypes(include=[np.number])

# correlation with the target 'quality'
correlation = num_feat.corr()
print(correlation['quality'].sort_values(ascending=False)[:10], '\n')
print(correlation['quality'].sort_values(ascending=False)[-10:], '\n')

# count the null values with panda
nulls = pd.DataFrame(dataset.isnull().sum().sort_values(ascending=False))
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

# managing a missing values
dataset = dataset.select_dtypes(include=[np.number]).interpolate().dropna()
print(sum(dataset.isnull().sum() != 0))

# build a linear model
y = np.log(dataset.quality)
X = dataset.drop(['quality'], axis=1)

# split the data with train_test_split method
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.33)

# fit linear regression
linear_r = linear_model.LinearRegression()
model = linear_r.fit(X_train, y_train)

# evaluate performances using from sklearn.metrics import mean_squared_error
# r-squared value is a measure of how close the data are to the fitted regression line
print("R Square is: \n", model.score(X_test, y_test))
predictions = model.predict(X_test)
# The RMSE measures the distance between our predicted values and actual values
print('RMSE is: \n', mean_squared_error(y_test, predictions))

# show the result - visualization-
actual_values = y_test
plt.scatter(predictions, actual_values, alpha=.70, color='r')
plt.xlabel('Predicted Quality')
plt.ylabel('Actual Quality')
plt.title('Linear Regression Model')
plt.show()
