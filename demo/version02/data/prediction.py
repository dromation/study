import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Collect data from table
data = pd.read_csv("data.csv")

# Separate data into features and target
X = data[["feature1", "feature2"]]
y = data["target"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Create a new table with predictions
new_table = pd.DataFrame({"ID": X_test["ID"], "Prediction": y_pred})

# Write predictions to a file
new_table.to_csv("predictions.csv", index=False)