import pandas as pd
import folium
from folium.plugins import HeatMap

# Define the path to the data file. Make sure the path is correct and adjust it according to your actual path.
data_path = 'C:\\Users\\mrtan\\Desktop\\OTOT_C\\world_air_quality.csv'

# Use pandas to load data. Assume that the field separator is a semicolon (;) .
air_quality_data = pd.read_csv(data_path, sep=';', on_bad_lines='skip')

# Extract coordinates, contaminants and values for heat maps. Ensure that the data does not contain missing values.
data_for_map = air_quality_data[['Coordinates', 'Pollutant', 'Value']].dropna()

# Split the coordinate field into latitude and longitude.
coordinates = data_for_map['Coordinates'].str.split(',', expand=True)
data_for_map['Latitude'] = coordinates[0].astype(float)
data_for_map['Longitude'] = coordinates[1].astype(float)

# Use the first coordinate point in the data as the center point of the map.
first_lat = data_for_map.iloc[0]['Latitude']
first_lon = data_for_map.iloc[0]['Longitude']

# Create a basic map.
map = folium.Map(location=[first_lat, first_lon], zoom_start=5)

# Add heat map layer. Here we use latitude, longitude, and values (pollutant concentrations).
HeatMap(data=data_for_map[['Latitude', 'Longitude', 'Value']], radius=10).add_to(map)

# Save the map as an HTML file that can be opened with a browser.
map.save('air_quality_heatmap.html')

print("地图已成功保存为 'air_quality_heatmap.html'。")

