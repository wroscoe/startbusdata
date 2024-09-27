import streamlit as st
import pandas as pd
import math
from pathlib import Path
from config import IMAGE_DIR
# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Start Bus Data Site',
    page_icon=':bus:', # This is an emoji shortcode. Could be a URL too.
)


'''
# :bus: START Data

Welcome to the community run START Bus and Transit data site. 

This is site a community run project to make it easier to browse and filter the START data. 
See the links in the sidebar to see data on [ridership](/Monthly_Ridership) and [financial](/Costs) data.

'''
image_path = IMAGE_DIR/'landing_demo.png'

st.image(str(image_path.absolute()), )

'''
### Data Sources: 

We've yet to figure out a way to get the data automatically, so for now we are manually collecting the data from the START Board meeting packets.

* Ridership data: collected from the monthly START Board meeting packets.
* Financial data: collected from the monthly START Board meeting packets.

You can see the raw data in repository [here](https://github.com/wroscoe/startbusdata/tree/main/data).



'''