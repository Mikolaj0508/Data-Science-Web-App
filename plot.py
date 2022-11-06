import pandas as pd
import numpy as np

def chart_data_prep(dataframe, area):
    dataframe.replace(["NaN", 'NaT'], np.nan, inplace = True)
    dataframe = dataframe.dropna()
    dataframe.groupby(['period'],dropna=True).mean()
    z = dataframe[dataframe.duoarea == area].sort_values('period')
    y = z.value
    x = z.period
    y.reset_index(drop=True, inplace=True)
    x.reset_index(drop=True, inplace=True)
    frames = [x,y]
    res = pd.concat(frames,axis=1)
    res.columns = ["Period","Value"]
    return res
