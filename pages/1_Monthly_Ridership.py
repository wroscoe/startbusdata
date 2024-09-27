import streamlit as st
import pandas as pd
import math
from pathlib import Path
from config import DATA_DIR
import dataloader

import altair as alt



# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='START Monthly Ridership',
    page_icon=':bus:', # This is an emoji shortcode. Could be a URL too.
)   

# -----------------------------------------------------------------------------
# Declare some useful functions.



df = dataloader.get_monthly_ridership_data()


# Set the title that appears at the top of the page.
'''
# :bus: START Monthly Ridership

Browse and filter the START Monthly Ridership data.
'''

# Add some spacing
''
''

with st.sidebar:
    min_value = df['Year'].min()
    max_value = df['Year'].max()

    from_year, to_year = st.slider(
        'Which years are you interested in?',
        min_value=min_value,
        max_value=max_value,
        value=[min_value, max_value])

    routes = df['Route'].unique()

    if not len(routes):
        st.warning("Select at least one country")

    selected_routes = st.multiselect(
        'Which routes would you like to view?',
        routes,
        routes)


    # Get unique months sorted
    unique_months = df['month'].sort_values().unique()
    month_options = df[['month', 'month_name']].drop_duplicates().sort_values('month')

    # Create a selectbox for month selection
    selected_month = st.sidebar.multiselect(
        'Select the month(s) you want to view',
        options=month_options['month_name'].tolist(),
        default=month_options['month_name'].tolist()
    )




    # Filter the data
    filtered_df = df[
        (df['Route'].isin(selected_routes))
        & (df['Year'] <= to_year)
        & (from_year <= df['Year'])
        & (df['month_name'].isin(selected_month))
    ]


first_year = df[df['Year'] == from_year]
last_year = df[df['Year'] == to_year]

st.header(f'Monthly Ridership Data', divider='gray')

''

# Create an Altair bar chart
bar_chart = alt.Chart(filtered_df).mark_bar().encode(
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



#SHOW YEAR OVER YEAR GROWTH

st.header(f'Year over Year Growth', divider='gray')

# Calculate the growth rate
growth_df = filtered_df[['Year', 'Riders']].groupby('Year').sum().reset_index()
growth_df['Growth'] = growth_df['Riders'].pct_change()

# Create an Altair bart chart

bar_chart_growth = alt.Chart(growth_df).mark_bar().encode(
    x='Year:O',
    y=alt.Y('Growth', title='Growth Rate'),
    color=alt.condition(
        alt.datum.Growth > 0,
        alt.value('green'),
        alt.value('red')
    )
).properties(
    title='Year over Year Growth',
    height=600
).configure_view(
    stroke=None,
)

st.altair_chart(bar_chart_growth, use_container_width=True)
