# 🍽️ Restaurant Rating Prediction System

## 📌 Project Overview

This project is a Machine Learning based Restaurant Rating Prediction System developed using Python and Scikit-learn.

The objective of this project is to predict the aggregate rating of restaurants using different restaurant features.

---

# 🎯 Objective

To build a machine learning model that predicts restaurant ratings based on:
- Average Cost for Two
- Votes
- Price Range
- Table Booking Availability
- Online Delivery Availability

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- VS Code

---

# 📂 Dataset Information

Dataset contains:
- Restaurant Name
- City
- Cuisines
- Votes
- Average Cost for Two
- Aggregate Rating
- Online Delivery
- Table Booking

Dataset Size:
- Rows: 9551
- Columns: 21

---

# ⚙️ Steps Performed

## 1. Data Loading
Loaded dataset using Pandas.

## 2. Data Cleaning
Handled missing values using `dropna()`.

## 3. Data Preprocessing
Converted categorical values into numerical values using Label Encoding.

## 4. Feature Selection
Selected important features:
- Average Cost for two
- Votes
- Price range
- Has Table booking
- Has Online delivery

## 5. Train-Test Split
Split data into:
- 80% Training Data
- 20% Testing Data

## 6. Model Training
Used:
- Linear Regression
- Decision Tree Regressor

## 7. Prediction
Predicted restaurant ratings.

## 8. Model Evaluation
Evaluated model using:
- Mean Squared Error (MSE)
- R² Score

## 9. Visualization
Created Actual vs Predicted Ratings graph.

---

# 📊 Model Performance

## Decision Tree Regressor
- Mean Squared Error: 0.20
- R² Score: 0.91

The Decision Tree Regressor performed better than Linear Regression.

---

# 📈 Feature Importance

Important features affecting ratings:
- Votes
- Average Cost for Two
- Price Range

---

# 📷 Output

The project generates:
- Predicted Ratings
- Accuracy Metrics
- Graph Visualization
- Saved Model File (`model.pkl`)

---

# 💾 Saved Model

The trained machine learning model is saved as:

model.pkl

---

# 🚀 How to Run the Project

## Step 1
Install required libraries:

pip install pandas numpy matplotlib seaborn scikit-learn

## Step 2
Place `dataset.csv` in the project folder.

## Step 3
Run the project:

python main.py

---

# 📁 Project Structure

Restaurant_Rating_Prediction/
│
├── dataset.csv
├── main.py
├── model.pkl
├── README.md
└── screenshots/

---

# ✅ Conclusion

This project successfully predicts restaurant ratings using Machine Learning techniques.

The Decision Tree Regressor achieved high accuracy and better performance compared to Linear Regression.

This project helped in understanding:
- Data preprocessing
- Feature engineering
- Regression algorithms
- Model evaluation
- Data visualization

---

# 👨‍💻 Developed By

Ashwitha Sunkaraneni
