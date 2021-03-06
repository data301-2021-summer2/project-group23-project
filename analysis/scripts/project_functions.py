#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[4]:


spy = "~/project-group23-project/data/raw/spy.csv"
tsla = "~/project-group23-project/data/raw/TSLA.csv"
# Making a function out of the method chaining
#function 1 Goal: clean, rename, drop necessary rows/columns from 2 dataframes.


def load_and_clean_tsla_spy(spy,tsla):
    tsladf = (pd.read_csv(tsla, parse_dates=["Date"])
              .drop(columns=["High","Low","Adj Close"])
              .rename(columns={"Open":"open_tsla","Close":"close_tsla","Volume":"vol_tsla"})
              .reset_index(drop=True))
    
    spydf = (pd.read_csv(spy, parse_dates=["Date"])
             .drop(columns=["High","Low","Adj Close"])
             .rename(columns={"Open":"open_spy","Close":"close_spy","Volume":"vol_spy"})
             .reset_index(drop=True))
    return (spydf,tsladf)

x=load_and_clean_tsla_spy(spy,tsla)

#SOURCES USED:
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html


# In[ ]:




