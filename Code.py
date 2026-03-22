# 📌 Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 📌 Step 2: Upload Dataset (Colab)
from google.colab import files
uploaded = files.upload()

# Replace filename if needed
df = pd.read_csv('house_data_linear.csv')

# 📌 Step 3: Display Data
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# 📌 Step 4: Data Preprocessing

# Handle missing values
df = df.dropna()

# Convert categorical columns into numerical (if any)
df = pd.get_dummies(df, drop_first=True)

# 📌 Step 5: Define Features and Target
# Assuming 'price' is target column (change if needed)
X = df.drop('price', axis=1)
y = df['price']

# 📌 Step 6: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 📌 Step 7: Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# 📌 Step 8: Predictions
y_pred = model.predict(X_test)

# 📌 Step 9: Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n📊 Model Evaluation:")
print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)

# 📌 Step 10: Visualization
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()

# 📌 Step 11: Sample Prediction
sample = X_test.iloc[0].values.reshape(1, -1)
predicted_price = model.predict(sample)

print("\nHouse Sample Prediction:", predicted_price[0])
