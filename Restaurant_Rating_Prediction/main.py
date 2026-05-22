import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("dataset.csv")

# Remove missing values
df.dropna(inplace=True)

# Label Encoding
le = LabelEncoder()

df['Has Table booking'] = le.fit_transform(df['Has Table booking'])
df['Has Online delivery'] = le.fit_transform(df['Has Online delivery'])
df['Is delivering now'] = le.fit_transform(df['Is delivering now'])
df['Switch to order menu'] = le.fit_transform(df['Switch to order menu'])

# Feature Selection
features = [
    'Average Cost for two',
    'Votes',
    'Price range',
    'Has Table booking',
    'Has Online delivery'
]

X = df[features]

# Target Column
y = df['Aggregate rating']

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Model
model = DecisionTreeRegressor(random_state=42)

# Train Model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Show Predictions
print("\nPredicted Ratings:\n")
print(predictions[:10])

# Evaluate Model
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Evaluation:\n")
print("Mean Squared Error:", mse)
print("R2 Score:", r2) 

import matplotlib.pyplot as plt

# Scatter Plot
plt.scatter(y_test, predictions)

# Labels
plt.xlabel("Actual Ratings")
plt.ylabel("Predicted Ratings")

# Title
plt.title("Actual vs Predicted Ratings")

# Show graph
plt.show() 
# Feature Importance

importance = model.feature_importances_

print("\nFeature Importance:\n")

for i, v in enumerate(importance):
    print(f"{features[i]} : {v}") 
    
    import pickle

# Save trained model
pickle.dump(model, open("model.pkl", "wb"))

print("\nModel saved successfully!")