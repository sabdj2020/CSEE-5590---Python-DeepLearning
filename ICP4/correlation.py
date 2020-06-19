# libraries

import pandas as pd

# read csv file using pd.read_csv available in panda

data = pd.read_csv("DataSet/train.csv")
print (data)
# find correlation
# we can quickly analyze our feature correlations by pivoting features against each other
# We can only do so at this stage for features which do not have any empty values. 

print(data.isnull().sum())

print(data[['Sex', 'Survived']].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False))