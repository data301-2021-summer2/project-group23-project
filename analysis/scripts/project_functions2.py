#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[13]:


#function 2 GOAL: remove unwanted dates from df.
from scripts import project_functions
spy = "~/project-group23-project/data/raw/spy.csv"
tsla = "~/project-group23-project/data/raw/TSLA.csv"
x=project_functions.load_and_clean_tsla_spy(spy,tsla)

spydf=x[0]

removeolder=pd.to_datetime("2010-06-28")
removenewer=pd.to_datetime("2020-02-04")
def remove_dates(spydf):
    
    spyclean = (pd.DataFrame(spydf)
               .loc[(spydf.Date > removeolder)]
                .loc[(spydf.Date < removenewer)]
                .reset_index(drop=True))
    
    return spyclean
y=remove_dates(spydf)


    

        


  


   





#SOURCES USED:
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html
#https://stackoverflow.com/questions/41513324/python-pandas-drop-rows-of-a-timeserie-based-on-time-range


# In[10]:





# In[ ]:




