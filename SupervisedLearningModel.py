from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import datasets
#pip install scikit-learn


# Load the Iris dataset
iris = datasets.load_iris()
x = iris.data
y = iris.target

# Print the feature names and data
print('Feature Names:', iris.feature_names)
print('Data:')
print(x)

# Print the class labels
print('Class Labels: 0 - Iris-Setosa, 1 - Iris-Versicolour, 2 - Iris-Virginica')
print('Labels:')
print(y)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# Create a KNN classifier with K=5
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)

# Make predictions on the test data
y_pred = classifier.predict(x_test)

# Print the confusion matrix
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))

# Print classification report (including precision, recall, F1-score, and support)
print('Accuracy Metrics:')
print(classification_report(y_test, y_pred))
