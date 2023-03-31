import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                           random_state=213, n_clusters_per_class=1, class_sep=1)

# a)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=5)

colors = ["orange", "green"]
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train,
            cmap=matplotlib.colors.ListedColormap(colors))
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, marker="x",
            cmap=matplotlib.colors.ListedColormap(colors))
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Training and testing data")
plt.show()

# b)
logisticRegression = LogisticRegression()
logisticRegression.fit(X_train, y_train)

# c)
theta = logisticRegression.intercept_
thete = logisticRegression.coef_
print(thete.shape)
a = -thete[0, 0]/thete[0, 1]
c = -theta/thete[0, 1]
x1x2min = X_train.min() - 0.5
x1x2max = X_train.max() + 0.5
xd = np.array([x1x2min, x1x2max])
yd = a*xd + c
plt.plot(xd, yd, linestyle='--')
plt.fill_between(xd, yd, x1x2min, color="orange", alpha=0.2)
plt.fill_between(xd, yd, x1x2max, color="green", alpha=0.2)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train,
            cmap=matplotlib.colors.ListedColormap(colors))
plt.xlim(x1x2min, x1x2max)
plt.ylim(x1x2min, x1x2max)
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Training data and border decision")
plt.show()

# d)
y_prediction = logisticRegression.predict(X_test)
cm = confusion_matrix(y_test, y_prediction)
disp = ConfusionMatrixDisplay(cm)
disp.plot()
plt.title("Confusion Matrix")
plt.show()
print("Accuracy: ", accuracy_score(y_test, y_prediction))
print("Precison: ", precision_score(y_test, y_prediction))
print("Recall: ", recall_score(y_test, y_prediction))

# e)
colorsEvaluation = ["black", "yellow"]
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test == y_prediction, cmap=matplotlib.colors.ListedColormap(
    colorsEvaluation))
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Prediction accuracy")
cbar = plt.colorbar(ticks=[0, 1])
cbar.ax.set_yticklabels(["False", "True"])
plt.show()
