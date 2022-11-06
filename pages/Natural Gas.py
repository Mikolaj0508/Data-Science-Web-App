import streamlit as st
import calendar

from scraping import scrap, scrap_inside
from download import filedownload
from plot import chart

st.set_page_config(layout="wide")

exp = st.expander("About")
exp.markdown("""On this page you could get data about Natural Gas price and consumption in all areas in USA. You have to specify what you like to see. Also you could specify time range.""")

col1 = st.sidebar
col1.header('Option Panel')

route_1 = col1.selectbox('Select desired topic', ('Prices','Consumption/End Use'))

primary_route,names = scrap(route_1)

route_2 = col1.radio('Select desired options', names.keys())


col1.write("---")

start_year,end_year,start_month,end_month = False,False,False,False

agree = col1.checkbox('Specify Date Range', value=False)

if agree:
    start_year, end_year = col1.select_slider(
    'Select a range of years',
    options=[i for i in range(1973,2023)],
    value=(1985,2002))

    col11, col12 = col1.columns(2)
    with col11:
      start_month = col11.radio("Month of start",(calendar.month_name[1:]),index=3)
    with col12:
      end_month = col12.radio("Month of end",(calendar.month_name[1:]),index=10)
    
    col1.write("---")

col1.write("---")


if st.button('Get data sample:'):
  second_route = scrap_inside(primary_route,names[route_2],start_y=start_year,start_m=start_month,end_y=end_year,end_m=end_month)[0]
  st.write(f"Dataframe is size {second_route.size} of cells and shape {second_route.shape}")
  st.table(second_route.tail())


if st.button('Get raw CSV file:'):
  st.markdown(filedownload(scrap_inside(primary_route,names[route_2],start_y=start_year,start_m=start_month,end_y=end_year,end_m=end_month)[0]), unsafe_allow_html=True)


agree_2 = st.checkbox('Pick desired area to plot chart', value=False)


if agree_2:
  second_route,areas = scrap_inside(primary_route,names[route_2],start_y=start_year,start_m=start_month,end_y=end_year,end_m=end_month)
  desired_area = st.selectbox('Pick desired area to plot chart', areas)


if 'desired_area' not in locals():
  st.warning('Please choose desired area')
  st.stop()
fr = chart_data_prep(second_route,desired_area)
st.line_chart(fr,x="Period",y="Value")









