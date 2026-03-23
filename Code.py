# Step 1: Install libraries
!pip install pandas numpy scikit-learn matplotlib

# Step 2: Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 3: Upload dataset (insurance.csv)
from google.colab import files
uploaded = files.upload()

import io
df = pd.read_csv(io.BytesIO(uploaded[list(uploaded.keys())[0]]))

# Step 4: Display dataset
print("First 5 rows:")
print(df.head())

# Step 5: Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# Step 6: Encoding categorical variables (One-Hot Encoding)
df = pd.get_dummies(df, drop_first=True)

# Step 7: Define features and target
X = df.drop('charges', axis=1)
y = df['charges']

# Step 8: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 9: Feature Scaling (important step)
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 10: Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 11: Predictions
y_pred = model.predict(X_test)

# Step 12: Evaluation
print("\nModel Performance:")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Step 13: Predict new data
# Example input: age, bmi, children, sex_male, smoker_yes, region_northwest, region_southeast, region_southwest
sample = [30, 25.3, 2, 1, 0, 0, 1, 0]

sample_scaled = scaler.transform([sample])
prediction = model.predict(sample_scaled)

print("\nPredicted Medical Cost:", prediction[0])

# Step 14: Visualization (Actual vs Predicted)
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Charges")
plt.ylabel("Predicted Charges")
plt.title("Actual vs Predicted Medical Costs")
plt.show()
