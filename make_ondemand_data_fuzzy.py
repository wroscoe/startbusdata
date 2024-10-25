import pandas as pd
import math
from config import DATA_DIR, HIDDEN_DATA_DIR

# Define the grid size in meters
grid_size_m = 50

def bin_to_grid(lat, lon, grid_size_m):
    # Approximate length of a degree of latitude in meters
    lat_degree_m = 111320
    # Approximate length of a degree of longitude in meters (varies by latitude)
    lon_degree_m = 80903

    # Calculate the grid size in degrees
    lat_grid_size = grid_size_m / lat_degree_m
    lon_grid_size = grid_size_m / lon_degree_m

    # Bin the latitude and longitude to the nearest grid point
    binned_lat = round(lat / lat_grid_size) * lat_grid_size
    binned_lon = round(lon / lon_grid_size) * lon_grid_size

    return binned_lat, binned_lon

# Load the dataset
source_filename = HIDDEN_DATA_DIR / 'ondemand.csv'
dest_filename = DATA_DIR / 'binned_ondemand.csv'
data = pd.read_csv(source_filename)

# Convert to DataFrame
df = pd.DataFrame(data)

# Apply grid binning to pickup and dropoff locations
for index, row in df.iterrows():
    binned_pickup_lat, binned_pickup_lon = bin_to_grid(row['pickup_lat'], row['pickup_lon'], grid_size_m)
    binned_dropoff_lat, binned_dropoff_lon = bin_to_grid(row['dropoff_lat'], row['dropoff_lon'], grid_size_m)

    df.at[index, 'pickup_lat'] = binned_pickup_lat
    df.at[index, 'pickup_lon'] = binned_pickup_lon
    df.at[index, 'dropoff_lat'] = binned_dropoff_lat
    df.at[index, 'dropoff_lon'] = binned_dropoff_lon

# Print the DataFrame with binned locations
print(df)

# Optionally, save the DataFrame to a CSV file
df.to_csv(dest_filename, index=False)
