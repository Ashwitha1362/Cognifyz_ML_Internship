# 🍽️ Restaurant Recommendation System

## 📌 Project Overview

This project is a Restaurant Recommendation System developed using Python and Pandas.

The system recommends restaurants to users based on:
- Preferred Cuisine
- Price Range
- Restaurant Ratings

The recommendation system uses content-based filtering to suggest restaurants similar to user preferences.

---

# 🎯 Objective

To create a restaurant recommendation system that provides personalized restaurant suggestions based on user preferences.

---

# 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn
- VS Code

---

# 📂 Dataset Information

Dataset contains:
- Restaurant Name
- Cuisines
- Price Range
- Aggregate Rating
- City
- Votes

Dataset Size:
- Rows: 9551
- Columns: 21

---

# ⚙️ Steps Performed

## 1. Data Loading
Loaded dataset using Pandas.

## 2. Data Cleaning
Handled missing values using `dropna()`.

## 3. User Preference Input
Accepted user preferences:
- Cuisine Type
- Price Range

## 4. Restaurant Filtering
Filtered restaurants based on:
- Matching cuisines
- Selected price range

## 5. Recommendation Ranking
Sorted restaurants using Aggregate Ratings.

## 6. Visualization
Created graph visualization for top recommended restaurants.

---

# 📊 Features

The system provides:
- Personalized recommendations
- Cuisine filtering
- Price range filtering
- Top-rated restaurant suggestions

---

# 📈 Output

The project generates:
- Recommended restaurant list
- Restaurant ratings
- Recommendation graph visualization

---

# 🚀 How to Run the Project

## Step 1
Install required libraries:

pip install pandas matplotlib scikit-learn

## Step 2
Place `dataset.csv` in the project folder.

## Step 3
Run the project:

python main.py

---

# 📁 Project Structure

Task_2_Restaurant_Recommendation/
│
├── dataset.csv
├── main.py
├── README.md
└── screenshots/

---

# ✅ Conclusion

This project successfully recommends restaurants based on user preferences using content-based filtering techniques.

The recommendation system provides personalized and highly rated restaurant suggestions according to cuisine and budget preferences.

---

# 👨‍💻 Developed By

Ashwitha Sunkaraneni