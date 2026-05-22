import pandas as pd
import folium

# Load dataset
df = pd.read_csv("dataset.csv")

# Remove missing values
df.dropna(inplace=True)

# Create base map
restaurant_map = folium.Map(
    location=[df['Latitude'].mean(), df['Longitude'].mean()],
    zoom_start=5
)

# Add restaurant markers
for index, row in df.head(100).iterrows():
    folium.Marker(
        [row['Latitude'], row['Longitude']],
        popup=row['Restaurant Name']
    ).add_to(restaurant_map)

# Save map
restaurant_map.save("restaurant_map.html")

print("\nMap created successfully!")
print("Open 'restaurant_map.html' to view the map.")