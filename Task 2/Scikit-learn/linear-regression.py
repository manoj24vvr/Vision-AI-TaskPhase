from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

boston = datasets.load_boston()

# features / labels
X = boston.data
y = boston.target

print("X")
print(X)
print(X.shape)
print("y")
print(y)
print(y.shape)

# algorithm
li_reg = linear_model.LinearRegression()

plt.scatter(X.T[5],y)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

# train
model = li_reg.fit(X_train,y_train)
predictions = model.predict(X_test)
print("Predictions: ",predictions)
print("R^2 score: ", li_reg.score(X,y))
print("coeff: ", li_reg.coef_)
print("Intercept: ", li_reg.intercept_)
