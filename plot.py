import pandas as pd
import matplotlib as plt
import streamlit as st

def chart(dataframe, area):
    fig, ax = plt.subplots()
    dataframe.dropna()
    #dataframe.fillna(method='backfill')
    dataframe.groupby(['period'],dropna=True).mean()
    z = dataframe[dataframe.duoarea == area].sort_values('period')
    y = dataframe.value[dataframe.duoarea == area]
    x = dataframe.period[dataframe.duoarea == area].sort_values()
    ax.plot(x,y)
    fig.autofmt_xdate()
    for tick in ax.get_xticklabels()[::2]:
      tick.set_visible(False)
    return fig,ax