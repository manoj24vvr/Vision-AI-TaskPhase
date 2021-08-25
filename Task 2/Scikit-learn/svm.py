from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
# split it in features and labels
X = iris.data
y = iris.target

classes = ['Iris Setosa','Iris Versicolour', 'Iris Vinginica']

print(X.shape)
print(y.shape)

# hours of study vs good/bad grades
# 10 different students
# train 8 students
# predict with the remaining 2
# level of accuracy

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#print(X_train.shape)
#print(X_test.shape)
#print(y_train.shape)
#print(y_test.shape)

model = svm.SVC()
model.fit(X_train,y_train)

print(model)

predictions = model.predict(X_test)
acc = accuracy_score(y_test,predictions)

print("Predictions: ",predictions)
print("actual: ",y_test)
print("Accuracy: ",acc)

for i in range(len(predictions)):
    print(classes[predictions[i]])
