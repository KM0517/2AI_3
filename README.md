# 🏥 Medical Cost Prediction using Linear Regression

## 📌 Project Overview

This project aims to predict individual medical insurance costs based on personal attributes such as age, BMI, smoking habits, and region. The model uses **Linear Regression**, a supervised machine learning algorithm, to estimate healthcare expenses.

---

## 🎯 Problem Statement

Medical insurance companies need to estimate the cost of insurance for individuals based on their personal and health-related information. This project builds a predictive model that helps in estimating medical charges using historical data.

---

## 📊 Dataset Information

The dataset contains the following features:

* **age**: Age of the individual
* **sex**: Gender (male/female)
* **bmi**: Body Mass Index
* **children**: Number of dependents
* **smoker**: Smoking status (yes/no)
* **region**: Residential area (southeast, southwest, northeast, northwest)
* **charges**: Medical insurance cost (target variable)

---

## ⚙️ Technologies Used

* Python 🐍
* Pandas
* NumPy
* Scikit-learn
* Matplotlib

---

## 🔄 Project Workflow

1. Data Collection
2. Data Preprocessing
3. Splitting dataset (Train/Test)
4. Model Building using Linear Regression
5. Model Evaluation
6. Prediction

---

## 🧹 Data Preprocessing Steps

Data preprocessing is an important step to prepare the dataset before applying machine learning algorithms. The following steps were performed:

1. **Handling Missing Values**

   * Checked for null or missing values in the dataset.
   * Removed or handled missing data using appropriate methods (e.g., dropping rows).

2. **Encoding Categorical Variables**

   * Converted categorical features such as *sex*, *smoker*, and *region* into numerical format.
   * Used techniques like **Label Encoding** or **One-Hot Encoding**.

3. **Feature Selection**

   * Selected relevant input features (age, BMI, children, etc.) and target variable (charges).
   * Removed unnecessary columns if present.

4. **Feature Scaling**

   * Applied **StandardScaler** to normalize numerical features.
   * Helps improve model performance by bringing all features to the same scale.

5. **Train-Test Split**

   * Divided dataset into training and testing sets (e.g., 80% training, 20% testing).
   * Ensures proper evaluation of model performance.

---

## 🤖 Model Used

**Linear Regression** is used to model the relationship between input features and medical charges. It predicts continuous values and is suitable for cost estimation problems.

---

## 📈 Evaluation Metrics

* **Mean Squared Error (MSE)**
* **R² Score (Coefficient of Determination)**

---

## 📌 Example Prediction

The model can predict medical charges for a new individual based on input features like age, BMI, and smoking status.

---

## 📚 Conclusion

This project demonstrates how machine learning can be used to estimate medical costs effectively. Linear regression provides a simple yet powerful approach for predicting continuous values such as insurance charges.

---

## 👨‍💻 Contributors

* Team Members (Add your names here)

---

## 📜 License

This project is for educational purposes only.

