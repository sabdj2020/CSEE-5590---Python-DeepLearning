from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.svm import LinearSVC

# reading the data
train = fetch_20newsgroups(subset='train', shuffle=True)
test = fetch_20newsgroups(subset='test', shuffle=True)

# feature engineering step--raw text data will be transformed into feature vectors. TF-IDF score represents the relative importance of a term in the document
tfidf_Vect = TfidfVectorizer(ngram_range=(1, 2), stop_words='english') # (1,2) means unigram and bigram
X_train_tfidf = tfidf_Vect.fit_transform(train.data)

# transformation of the test data using transform
X_test_tfidf = tfidf_Vect.transform(test.data)

# Model Building ---train a classifier using the features created in the previous step.
classifier = MultinomialNB()
classifier.fit(X_train_tfidf, train.target)
# evaluate the model
predicted = classifier.predict(X_test_tfidf)

score = metrics.accuracy_score(test.target, predicted)
print("Multinomial NB classifier model accuracy is: ", score)

# create svm using LinearSVC()
svm = LinearSVC()

# train the model using fit() method
svm.fit(X_train_tfidf, train.target)

# Evaluation of the model
predicted = svm.predict(X_test_tfidf)
# print the accuracy score for the SVM model
svm_score = metrics.accuracy_score(test.target, predicted)
print("svm model accuracy is: ", svm_score)

