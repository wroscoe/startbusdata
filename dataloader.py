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

    df['fiscal_year'] = df['date'].apply(calculate_fiscal_year_from_date)

 
    return df



@st.cache_data
def get_cost_data():

    # Load csv with columns Description,Year,Status,Amount,CATEGORY

    DATA_FILENAME = DATA_DIR/'costs.csv'
    df = pd.read_csv(DATA_FILENAME)

 
    return df


@st.cache_data
def get_cost_per_ride_data():
    ridership = get_monthly_ridership_data()
    costs = get_cost_data()

    #group ridership data by fiscal year 
    ridership = ridership.groupby(['fiscal_year'])['Riders'].sum().reset_index()
    #group cost data by fiscal year
    costs = costs.groupby(['Fiscal Year','Category'])['Amount'].sum().reset_index()

    #join the two dataframes
    costs = costs.merge(ridership, left_on='Fiscal Year', right_on='fiscal_year', how='outer')

    #calculate cost per ride
    costs['cost_per_ride'] = costs['Amount']/costs['Riders']

    #round to 2 decimal places
    costs['cost_per_ride'] = costs['cost_per_ride'].round(2)



    return costs



def calculate_fiscal_year_from_date(date):
    # Fiscal year starts on July 1st
    if date.month >= 7:
        return date.year + 1
    else:
        return date.year