import streamlit as st
import pandas as pd
import math
from pathlib import Path

from config import DATA_DIR

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Financial dashboard',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.
st.header('Financial Data')