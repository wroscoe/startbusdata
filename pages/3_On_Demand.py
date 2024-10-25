import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap
from io import StringIO
from config import DATA_DIR
from dataloader import get_on_demand_data

# Sample data
# Set Streamlit layout to wide
st.set_page_config(layout='wide')
data = get_on_demand_data()

# Create a Streamlit app
st.title('Ride Heatmap Visualization')
st.write('''
This app displays the June 2024 pickup and dropoff locations 
of on-demand rides as two different color heatmaps. The locations are rounded to the nearest 50 meters.
''')

# Hour selection in sidebar
pickup_hours = st.sidebar.multiselect('Select Pickup Hour(s) (select between 0 and 23)', options=list(range(24)), default=[6, 7, 8])
filtered_data = data[data['pickup_hour'].isin(pickup_hours)]

# Toggle options in sidebar to display/hide heatmaps
show_pickup_heatmap = st.sidebar.checkbox('Show Pickup Heatmap', value=True)
show_dropoff_heatmap = st.sidebar.checkbox('Show Dropoff Heatmap', value=True)

# Define map center (average of pickup locations)
center_lat = filtered_data['pickup_lat'].mean()
center_lon = filtered_data['pickup_lon'].mean()

# Create a folium map
map_ = folium.Map(location=[center_lat, center_lon], zoom_start=13)

# Add pickup heatmap layer if selected
if show_pickup_heatmap:
    pickup_points = filtered_data[['pickup_lat', 'pickup_lon']].values.tolist()
    HeatMap(pickup_points, name='Pickups', gradient={0.4: 'blue', 0.65: 'cyan', 1: 'lime'}).add_to(map_)

# Add dropoff heatmap layer if selected
if show_dropoff_heatmap:
    dropoff_points = filtered_data[['dropoff_lat', 'dropoff_lon']].values.tolist()
    HeatMap(dropoff_points, name='Dropoffs', gradient={0.4: 'red', 0.65: 'orange', 1: 'yellow'}).add_to(map_)

# Add layer control
folium.LayerControl().add_to(map_)

# Display map in Streamlit
folium_static(map_)
