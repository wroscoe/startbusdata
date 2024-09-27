import streamlit as st
import pandas as pd
import math
from pathlib import Path
import dataloader

from config import DATA_DIR

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Financial dashboard',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.
st.header('Financial Data')


df = dataloader.get_cost_data()


with st.sidebar:


    #filter by category
    categories = df['Category'].unique()
    selected_categories = st.multiselect(
        'Which categories would you like to view?',
        categories,
        categories)



# Chart shoing the total cost per year

st.write('Total cost per year')
yearly_costs = df.groupby('Year')['Amount'].sum()
st.bar_chart(yearly_costs)
