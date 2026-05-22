import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

# Remove missing values
df.dropna(inplace=True)

# Take user input
preferred_cuisine = input("Enter preferred cuisine: ")
preferred_price = int(input("Enter preferred price range (1-4): "))

# Filter restaurants
recommended = df[
    (df['Cuisines'].str.contains(preferred_cuisine, case=False)) &
    (df['Price range'] == preferred_price)
]

# Sort by ratings
recommended = recommended.sort_values(
    by='Aggregate rating',
    ascending=False
)

# Show recommendations
print("\nRecommended Restaurants:\n")

print(
    recommended[
        ['Restaurant Name', 'Cuisines', 'Price range', 'Aggregate rating']
    ].head(10)
)
import matplotlib.pyplot as plt

# Top 5 recommendations
top5 = recommended.head(5)

# Create graph
plt.figure(figsize=(10,6))

plt.bar(
    top5['Restaurant Name'],
    top5['Aggregate rating']
)

# Labels
plt.xlabel("Restaurant Name")
plt.ylabel("Aggregate Rating")

# Title
plt.title("Top Recommended Restaurants")

# Rotate names
plt.xticks(rotation=45)

# Show graph
plt.show()