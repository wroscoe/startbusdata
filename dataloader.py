import pandas as pd
from pathlib import Path
from config import DATA_DIR

import streamlit as st

@st.cache_data
def get_monthly_ridership_data():

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = DATA_DIR/'monthly_ridership.csv'
    df = pd.read_csv(DATA_FILENAME)


    # Extract month names from the data
    # convert to datetime
    df['date'] = pd.to_datetime(df['Date'])
    df['month'] = df['date'].dt.month
    df['month_name'] = df['date'].dt.strftime('%B')

 
    return df



@st.cache_data
def get_cost_data():

    # Load csv with columns Description,Year,Status,Amount,CATEGORY

    DATA_FILENAME = DATA_DIR/'costs.csv'
    df = pd.read_csv(DATA_FILENAME)

 
    return df