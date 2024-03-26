import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data_path = 'C:\\Users\\mrtan\\Desktop\\OTOT_C\\world_air_quality.csv'  
air_quality_data = pd.read_csv(data_path, sep=';')

def visualize_specific_pollutant(data, pollutant_filter, top_n=10):
    """
    Visualize the top N countries with the highest average pollution levels
    for a specific pollutant in the dataset.
    
    Parameters:
    - data: The air quality dataset.
    - pollutant_filter: The specific pollutant to visualize.
    - top_n: The number of top countries to display.
    """
    # Filter by the specified pollutant
    filtered_data = data[data['Pollutant'] == pollutant_filter]
    
    # Calculate the average pollution value by country for the specified pollutant
    country_avg_pollution = filtered_data.groupby('Country Label')['Value'].mean().sort_values(ascending=False)
    
    # Select the top N countries with the highest average pollution level
    top_countries = country_avg_pollution.head(top_n)
    
    # Plotting
    plt.figure(figsize=(12, 8))
    sns.barplot(x=top_countries.values, y=top_countries.index, palette="coolwarm")
    plt.title(f'Top {top_n} Countries with Highest Average {pollutant_filter} Level')
    plt.xlabel('Average Pollution Value (ppm)')
    plt.ylabel('Country')
    plt.grid(axis='x')
    
    plt.show()


visualize_specific_pollutant(air_quality_data, 'O3', 10)

