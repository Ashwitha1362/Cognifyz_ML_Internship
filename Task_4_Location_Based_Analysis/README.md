# 📍 Location-Based Restaurant Analysis

## 📌 Project Overview

This project performs a geographical and statistical analysis of restaurants using restaurant dataset information.

The objective is to analyze restaurant distribution, ratings, and locations using data visualization and map analysis techniques.

---

# 🎯 Objective

To perform location-based analysis of restaurants by:
- Exploring latitude and longitude coordinates
- Analyzing restaurant concentration by city
- Comparing average restaurant ratings across cities
- Visualizing restaurant locations on an interactive map

---

# 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Folium
- VS Code

---

# 📂 Dataset Information

Dataset contains:
- Restaurant Name
- City
- Latitude
- Longitude
- Aggregate Rating
- Cuisines
- Price Range

Dataset Size:
- Rows: 9551
- Columns: 21

---

# ⚙️ Steps Performed

## 1. Data Loading
Loaded dataset using Pandas.

## 2. Data Cleaning
Handled missing values using `dropna()`.

## 3. City Analysis
Calculated the number of restaurants available in each city.

## 4. Restaurant Concentration Visualization
Created a bar graph for top cities with most restaurants.

## 5. Average Ratings Analysis
Calculated average restaurant ratings city-wise.

## 6. Rating Visualization
Created a bar chart for cities with highest average ratings.

## 7. Map Visualization
Used Folium to create an interactive restaurant location map.

---

# 📊 Key Insights

- New Delhi has the highest number of restaurants in the dataset.
- Some cities have significantly higher average ratings than others.
- Restaurant distribution is heavily concentrated in a few major cities.

---

# 📈 Visualizations

The project includes:
- Restaurant concentration graph
- Average ratings graph
- Interactive restaurant map

---

# 📍 Interactive Map

The interactive restaurant location map is saved as:

restaurant_map.html

---

# 🚀 How to Run the Project

## Step 1
Install required libraries:

pip install pandas matplotlib folium

## Step 2
Place `dataset.csv` in the project folder.

## Step 3
Run the project:

python main.py

---

# 📁 Project Structure

Task_4_Location_Based_Analysis/
│
├── dataset.csv
├── main.py
├── restaurant_map.html
├── README.md
└── screenshots/

---

# ✅ Conclusion

This project successfully analyzed restaurant locations and geographical patterns using Python visualization libraries.

The project provided insights into:
- Restaurant distribution
- City-wise restaurant concentration
- Average ratings by city
- Interactive map-based restaurant visualization

---

# 👨‍💻 Developed By

Ashu