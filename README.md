# 🏠 House Price Prediction
Team Number : 2AI_3 Project Objective: Predict individual house's price.

## 📌 Problem Statement

The goal of this project is to build a machine learning model that can predict house prices based on various features such as location, size, number of bedrooms, and other relevant factors. Accurate house price prediction helps buyers, sellers, and real estate agents make informed decisions.

---

## 🎯 Objectives

* Analyze housing data to identify important features affecting price
* Build a predictive model using machine learning algorithms
* Evaluate model performance using appropriate metrics
* Provide accurate price predictions for new data

---

## 📊 Dataset Description

The dataset typically includes the following features:

* Area (in square feet)
* Number of bedrooms
* Number of bathrooms
* Location
* Age of the house
* Amenities (parking, garden, etc.)

Target Variable:

* House Price

---

## ⚙️ Technologies Used

* Python
* Google Colab / Jupyter Notebook
* NumPy
* Pandas
* Matplotlib / Seaborn
* Scikit-learn

---

## 🧠 Data Preprocessing Steps

1. Data Collection
2. Data Preprocessing

   * Handling missing values (mean/median imputation or dropping rows)
   * Removing duplicates
   * Encoding categorical variables (One-Hot Encoding / Label Encoding)
   * Feature scaling (Standardization or Normalization)
   * Outlier detection and removal
   * Splitting dataset into training and testing sets
3. Exploratory Data Analysis (EDA)
4. Model Building

   * Linear Regression
   * (Optional) Decision Trees / Random Forest
5. Model Evaluation

   * Mean Absolute Error (MAE)
   * Mean Squared Error (MSE)
   * R² Score

---

## 🧹 Detailed Dataset Preprocessing Steps

1. **Data Cleaning**

   * Identify and handle missing/null values
   * Remove duplicate records

2. **Handling Missing Values**

   * Numerical columns → fill with mean/median
   * Categorical columns → fill with mode or most frequent value

3. **Encoding Categorical Data**

   * Convert location and other categorical features into numerical form
   * Use One-Hot Encoding for nominal data

4. **Feature Scaling**

   * Apply StandardScaler or MinMaxScaler to normalize data
   * Helps improve model performance

5. **Outlier Detection**

   * Use boxplots or IQR method
   * Remove extreme values that can skew predictions

6. **Feature Selection**

   * Select important features using correlation analysis
   * Remove irrelevant or highly correlated features

7. **Train-Test Split**

   * Split dataset (e.g., 80% training, 20% testing)
   * Ensures model generalization

---

## 📈 Expected Outcome

* A trained machine learning model capable of predicting house prices
* Insights into key factors influencing housing prices

---

## 🔮 Future Improvements

* Use advanced models like XGBoost or Neural Networks
* Deploy the model as a web application
* Integrate real-time housing data

---

## 👨‍💻 Author

* Khyati Sri

---

## 📜 License

This project is open-source and available under the MIT License.
