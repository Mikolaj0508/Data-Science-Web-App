import requests
from key import api_key_v2
import pandas as pd
import calendar
import streamlit as st

def scrap(route):
    di = {
        'Consumption/End Use':'cons',
        'Prices':'pri'
    }
    url = f'http://api.eia.gov/v2/natural-gas/{di[route]}?api_key={api_key_v2}'
    r = requests.get(url)
    json_data = r.json()
    di_names_id = {i["name"]:i["id"] for i in json_data["response"]["routes"]}
    return di[route],di_names_id

calendarr = calendar.month_name[1:]

@st.cache
def scrap_inside(name,id,**kwargs):
    if id in ("num","pns","acct"):
        if all(item is False for item in kwargs.values()):
            url = f"http://api.eia.gov/v2/natural-gas/{name}/{id}/data?api_key={api_key_v2}&data[]=value&frequency=annual"
        else:
            url = f"http://api.eia.gov/v2/natural-gas/{name}/{id}/data?api_key={api_key_v2}&data[]=value&frequency=annual&start={kwargs['start_y']}&end={kwargs['end_y']}"
    
    else:
        if all(item is False for item in kwargs.values()):
            url = f"http://api.eia.gov/v2/natural-gas/{name}/{id}/data?api_key={api_key_v2}&data[]=value&frequency=monthly"
        else:
            url = f"http://api.eia.gov/v2/natural-gas/{name}/{id}/data?api_key={api_key_v2}&data[]=value&frequency=monthly&start={kwargs['start_y']}-{calendarr.index(kwargs['start_m']):02}-31&end={kwargs['end_y']}-{calendarr.index(kwargs['start_m']):02}-01"
    r = requests.get(url)
    json_data = r.json()
    df = pd.DataFrame(json_data['response']['data'])
    df.sort_index(inplace=True)
    if id!="pns":
        df = df.loc[(df.units != "%")]
    areas = df['duoarea'].unique().tolist()
    return df,areas
