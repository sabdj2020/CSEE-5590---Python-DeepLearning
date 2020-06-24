# Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# step1: acquire the data and create our environment
# setting the plotting default
plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (12, 8)
# import data
dataset = pd.read_csv('dataset/train.csv')
print("the 10th record\n", dataset.head(10))

# step2: explore the data

# plot GarageArea field and SalePrice in scatter plot and show i graph show()
garage_area = dataset['GarageArea']
sale_price = dataset['SalePrice']
plt.scatter(garage_area, sale_price, alpha=.70, color='b')
plt.xlabel('Garbage Area')
plt.ylabel('Sale Price')
plt.show()

# describe features and get the statistics about feature and target value
print("\nStatistics about the dataframe")
print(dataset[['GarageArea','SalePrice']].describe())

# filter outliers
no_outliers = dataset['GarageArea'] <= 800
dataset = dataset[no_outliers]
no_outliers = dataset['GarageArea'] > 180
dataset = dataset[no_outliers]
no_outliers = dataset['GarageArea'] != 0
dataset = dataset[no_outliers]

# plot data without outliers and show the result in graph show()
garage_field = dataset['GarageArea']
sale_price = dataset['SalePrice']
plt.scatter(garage_field, sale_price, alpha=.70, color='y')
plt.xlabel('Garbage Area')
plt.ylabel('Sale Price')
plt.show()
