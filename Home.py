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

with st.sidebar:
    st.warning("Use these links above to find the data you're looking for.")


'''
# :bus: START Data

Welcome to the community run START Bus and Transit data site. The goal of this site is to make it easier 
to browse the START data in order to find problems and solutions. 


'''

st.info('''Use links in the left side menu to open reports on [ridership](/Monthly_Ridership), [financial](/Costs) and more.''')

image_path = IMAGE_DIR/'landing_demo.png'

st.image(str(image_path.absolute()), )

'''
### Data Sources: 

We'd love for this site to be updated monthly by the START team but for now we are manually updating the data.

* Ridership data: collected from the monthly START Board meeting packets.
* Financial data: collected from the monthly START Board meeting packets.

You can see the raw data in repository [here](https://github.com/wroscoe/startbusdata/tree/main/data).



'''