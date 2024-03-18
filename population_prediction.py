#world population Prediction
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

# Load the population projections data from the United Nations website
population_projections = pd.read_csv("https://population.un.org/wpp/Download/Files/1_Indicators_(WPP2022)/CSV_FILES/WPP2022_F03_POPULATION_BY_COUNTRY_2020-2100.CSV")

# Filter the data to only include countries and the predicted population in 2050, 2100, and 2200
filtered_data = population_projections[population_projections["Year"].isin([2050, 2100, 2200])]

# Create a GeoDataFrame from the data
gdf = gpd.GeoDataFrame(filtered_data, geometry=gpd.points_from_xy(filtered_data["LON"], filtered_data["LAT"]))

# Set the colormap
cmap = plt.cm.YlOrRd

# Create a choropleth map of the predicted population in 2050, 2100, and 2200
fig, ax = plt.subplots(figsize=(10, 10))

ax.axis("off")

# Plot the choropleth map
gdf.plot(column="PopTotal", cmap=cmap, ax=ax, edgecolor="white")

# Add a title and subtitle
ax.set_title("Predicted Population in 2050, 2100, and 2200")
ax.set_subtitle("World Population by Country")

# Add a legend
ax.legend(title="Population", loc="lower left")

# Save the figure
plt.savefig("population_prediction_2050_2100_2200.png")

# Create a bar chart of the predicted population in 2050, 2100, and 2200
fig, ax = plt.subplots(figsize=(10, 10))

# Sort the data by predicted population in 2200
filtered_data = filtered_data.sort_values(by=["PopTotal"], ascending=False)

# Get the country names and predicted population
country_names = filtered_data["Country"].tolist()
predicted_population = filtered_data["PopTotal"].tolist()

# Create a bar chart
ax.bar(country_names, predicted_population)

# Add a title and subtitle
ax.set_title("Predicted Population in 2050, 2100, and 2200")
ax.set_subtitle("World Population by Country")

# Rotate the x-axis labels to prevent overlapping
ax.set_xticklabels(country_names, rotation=90)

# Add a legend
ax.legend(title="Population", loc="lower left")

# Save the figure
plt.savefig("population_prediction_2050_2100_2200_bar_chart.png")
