# 📌 Day 31 — ML Pipeline + Train/Test Split
# 🎯 Learn:
## What is ML? Supervised vs Unsupervised
## Features & labels
## ML pipeline basics
## Train/Test split (why needed)
# 🧪 Practice:
## Load any dataset (I can give you one)
## Split it into train/test using train_test_split
## Print shapes → verify correct split
# 💻 Code tasks:
## Load the Iris dataset
## Use train/test split
## Train a simple KNN classifier
## Predict & print accuracy
## KNN, Linear Regression, Logistic Regression in this module

# Import necessary libraries
from sklearn.datasets import load_iris # Import Iris dataset
from sklearn.model_selection import train_test_split # For train/test split
from sklearn.neighbors import KNeighborsClassifier # KNN Classifier
from sklearn.metrics import accuracy_score # For accuracy calculation
import numpy as np # For numerical operations

# Load the Iris dataset
iris = load_iris() # it is present in sklearn.datasets
X = iris.data # Features eg sepal length, sepal width, petal length, petal width
y = iris.target # Labels eg species of iris flower
# Print dataset shape
print("Features shape:", X.shape) # (150, 4)
print("Labels shape:", y.shape) # (150,)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # 80% train, 20% test # x is features, y is labels test size is 20% of data and random state is for reproducibility
# Print shapes to verify correct split
print("X_train shape:", X_train.shape) # (120, 4) # what this shape means is 120 samples and 4 features
print("X_test shape:", X_test.shape) # (30, 4)
print("y_train shape:", y_train.shape) # (120,)
print("y_test shape:", y_test.shape) # (30,)

# Create and train the KNN classifier
knn = KNeighborsClassifier(n_neighbors=3) # Create KNN classifier with 3 neighbors meaning it will look at 3 nearest neighbors to classify a point
knn.fit(X_train, y_train) # Train the classifier
# Make predictions on the test set
y_pred = knn.predict(X_test) # Predict labels for test set
# Calculate and print the accuracy
accuracy = accuracy_score(y_test, y_pred) # Calculate accuracy
print("Accuracy of KNN classifier:", accuracy) # Print accuracy
# Example Output:
# Features shape: (150, 4)
# Labels shape: (150,)
# X_train shape: (120, 4)
# X_test shape: (30, 4)
# y_train shape: (120,)
# y_test shape: (30,)
# Accuracy of KNN classifier: 1.0


# Use California Housing dataset instead of the deprecated Boston dataset
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the California housing dataset
california = fetch_california_housing()
X_cal = california.data
y_cal = california.target

# Split the dataset into training and testing sets
Xc_train, Xc_test, yc_train, yc_test = train_test_split(X_cal, y_cal, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
lr = LinearRegression()
lr.fit(Xc_train, yc_train)

# Make predictions on the test set
yc_pred = lr.predict(Xc_test)

# Calculate and print the Mean Squared Error
mse = mean_squared_error(yc_test, yc_pred)
print("Mean Squared Error of Linear Regression (California housing):", mse)

# Logistic Regression example using Iris dataset
from sklearn.linear_model import LogisticRegression
# Create and train the Logistic Regression model
log_reg = LogisticRegression(max_iter=200)
log_reg.fit(X_train, y_train)
# Make predictions on the test set
y_log_pred = log_reg.predict(X_test)
# Calculate and print the accuracy
log_accuracy = accuracy_score(y_test, y_log_pred)
print("Accuracy of Logistic Regression classifier:", log_accuracy)
# Example Output:
# Mean Squared Error of Linear Regression (California housing): <some_value>  
# Accuracy of Logistic Regression classifier: <some_value>
# Note: The actual MSE and accuracy values will depend on the dataset and random state.