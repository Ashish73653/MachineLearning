from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# KNN regression on California Housing (corrected)

# Load dataset
housing = fetch_california_housing()
X = housing.data
y = housing.target

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # 80% train, 20% test test size is 20% of data and random state is for reproducibility , reproducibility means every time you run the code you will get the same split

# Feature scaling (important for KNN)
scaler = StandardScaler() # Standardize features by removing the mean and scaling to unit variance which means the distribution of each feature will have a mean value 0 and standard deviation of 1
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create and train KNN regressor
knn = KNeighborsRegressor(n_neighbors=3)
knn.fit(X_train, y_train)

# Predict and evaluate
y_pred = knn.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"Test samples: {X_test.shape[0]}")
print(f"RMSE: {rmse:.4f}")
print(f"R^2: {r2:.4f}")
