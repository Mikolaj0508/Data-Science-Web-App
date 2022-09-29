import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
import matplotlib.ticker as ticker
from PIL import Image

image = Image.open('src\logo.png')
st.set_page_config(page_title='Energy Resources Web App', initial_sidebar_state = 'auto')


st.image(image, use_column_width=True)

#---------------------------------#

st.title("Data Science Web App")

#---------------------------------#

st.markdown("""
This app retrieves energy resources data for the coal and natural gas usage!
""")

expander_bar = st.expander("Details")
expander_bar.markdown("""
* **Python libraries:** base64, pandas, streamlit, matplotlib, requests, json, 
* **Data source:** [U.S. Energy Information Administration (EIA)](https://www.eia.gov).
""")

st.write("\n\n")

st.write("""
**Data Science Web App** is simply web application which scraps Natural Gas data from U.S. Energy Information Administration (EIA). It uses RESTAPI to get information from EIA Website. Web App functionality is provided by Streamlit framework. Data preparation is possible due to Pandas.
""")

st.sidebar.write('''
* **[LinkedIn Profile](www.linkedin.com/in/mikołaj-wieczorkowski)**
* **[GitHub Profile](https://github.com/Mikolaj0508)**
''')

st.sidebar.write("---")

st.sidebar.write('''
**📩** mikolaj.wiecz20@gmail.com''')
st.sidebar.write('''
**📞** +48 792 074 044 ''')