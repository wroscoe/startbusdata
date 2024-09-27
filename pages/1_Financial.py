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



#update the dataframe to only include the selected categories
df = df[df['Category'].isin(selected_categories)]



# Chart shoing the total cost per year

st.write('Total cost per year')
#show chart with total cost per year divide costs by category

st.bar_chart(df[['Year', 'Description', 'Category', 'Amount', ]], x='Year', y='Amount', color='Category')



cost_detail_by_year = df.groupby(['Year', 'Description'])['Amount'].sum().reset_index().pivot(index='Description', columns='Year', values='Amount').fillna(0)


st.dataframe(cost_detail_by_year)
