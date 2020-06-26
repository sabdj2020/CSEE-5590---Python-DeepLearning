# import libraries
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# Read the data using pd.read_csv from panda library
dataset = pd.read_csv('dataset/CC.csv')
print(dataset.head(5))

# see how many samples we have of each tenure(how many classes we have in target)
print("**************************************")
print(dataset["TENURE"].value_counts())

# count the null values with panda
print("**************************************")
print("*count the number of null values for each feature*")
nulls = pd.DataFrame(dataset.isnull().sum().sort_values(ascending=False))
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

# fixing null values by replacing null values by mean for MINIMUM_PAYMENTS(313 null values) and CREDIT_LIMIT (1 null value)
dataset.loc[(dataset['MINIMUM_PAYMENTS'].isnull()==True),'MINIMUM_PAYMENTS']=dataset['MINIMUM_PAYMENTS'].mean()
dataset.loc[(dataset['CREDIT_LIMIT'].isnull()==True),'CREDIT_LIMIT']=dataset['CREDIT_LIMIT'].mean()

# count the null values with panda after replacing MINIMUM_PAYMENTS (313 null values) and CREDIT_LIMIT(1 null value)
print("**************************************")
print("null values after replacement")
nulls = pd.DataFrame(dataset.isnull().sum().sort_values(ascending=False))
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

# print data shape
print("**************************************")
print("this is the data shape")
x = dataset.iloc[:,1:-1]
y = dataset.iloc[:-1]
print(x.shape,y.shape)

# Use the elbow method to find a good number of clusters with the KMeans algorithm
wcss = []  #Within Cluster Sum of Squares

#elbow method to know the number of clusters # from sklearn.cluster import KMeans
for i in range(1,10):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

print("the wcss")
print(wcss)
plt.plot(range(1,10),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
print("*************************************")
print("find the optimal cluster")
plt.show()

# elbow method found that the number of clusters optimal is 3
nclusters = 3    # this is the k in kmeans
seed = 0
km = KMeans(n_clusters=nclusters, random_state=seed)
km.fit(x)   # predict the cluster for each data point
y_cluster_kmeans = km.predict(x)

# calculate the silhouette score # from sklearn import metrics
print("*********************************************************")
print("silhouette score before scaling**************************************")
from sklearn import metrics
score = metrics.silhouette_score(x, y_cluster_kmeans)
print(score)

# Try feature scaling to see if it will improve the Silhouette score #from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x)
x_scaler = scaler.transform(x)

km = KMeans(n_clusters=3)
km.fit(x_scaler)
y_cluster_kmeans = km.predict(x_scaler)
score = metrics.silhouette_score(x_scaler, y_cluster_kmeans)
print("silhouette score after scaler")
print(score)

# Apply PCA on the same dataset.

pca = PCA(3)
x_pca = pca.fit_transform(x_scaler)
df = pd.DataFrame(data=x_pca)
fdf = pd.concat([df,dataset[['TENURE']]],axis=1)
print("the PCA APPLIED")
print(fdf)
print("**********************************************")

# apply kmean on the PCA results
print(" KMEAN on PCA results")
km = KMeans(n_clusters=3)
km.fit(x_pca)
y_cluster_kmeans = km.predict(x_pca)
score = metrics.silhouette_score(x_pca, y_cluster_kmeans)
print(" KMEAN + PCA score is")
print(score)



