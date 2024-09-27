import streamlit as st
import pandas as pd
import math
from pathlib import Path
from config import DATA_DIR

import altair as alt



# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='START Monthly Ridership',
    page_icon=':bus:', # This is an emoji shortcode. Could be a URL too.
)   

# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data
def get_gdp_data():

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = DATA_DIR/'start_monthly_ridership_data.csv'
    raw_gdp_df = pd.read_csv(DATA_FILENAME)


    return raw_gdp_df

gdp_df = get_gdp_data()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# :bus: START Monthly Ridership

Browse and filter the START Monthly Ridership data.
'''

# Add some spacing
''
''

with st.sidebar:
    min_value = gdp_df['Year'].min()
    max_value = gdp_df['Year'].max()

    from_year, to_year = st.slider(
        'Which years are you interested in?',
        min_value=min_value,
        max_value=max_value,
        value=[min_value, max_value])

    routes = gdp_df['Route'].unique()

    if not len(routes):
        st.warning("Select at least one country")

    selected_routes = st.multiselect(
        'Which routes would you like to view?',
        routes,
        routes)


    # Filter the data
    filtered_gdp_df = gdp_df[
        (gdp_df['Route'].isin(selected_routes))
        & (gdp_df['Year'] <= to_year)
        & (from_year <= gdp_df['Year'])
    ]



first_year = gdp_df[gdp_df['Year'] == from_year]
last_year = gdp_df[gdp_df['Year'] == to_year]

st.header(f'Monthly Ridership Data', divider='gray')

''

# Create an Altair bar chart
bar_chart = alt.Chart(filtered_gdp_df).mark_bar().encode(
    xOffset='Year:O',
    x=alt.X('Route:O', axis=alt.Axis(labelAngle=-65)),
    y=alt.Y('Riders', title='Riders'),
    color='Year:O'  # Optional: Adds different colors for each bar
).properties(
    title='Sample Bar Chart',
    height=600
).configure_view(
    stroke=None,
)
st.altair_chart(bar_chart, use_container_width=True)

