#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[19]:


#function 3: merge the cleaned dataframes
from scripts import project_functions,project_functions2
spy = "~/project-group23-project/data/raw/spy.csv"
tsla = "~/project-group23-project/data/raw/TSLA.csv"
x=project_functions.load_and_clean_tsla_spy(spy,tsla)

spydf=x[0]

y=project_functions2.remove_dates(spydf)

spydf=y
tsladf=x[1]
tslaspymerged=(spydf,tsladf)

def merge_n_round(tslaspymerged):
    
    tslaspymerged = (pd.DataFrame(pd.merge(spydf,tsladf, how = 'inner'))
                     .round(decimals=2))
    return tslaspymerged
z=merge_n_round(tslaspymerged)


    

        


  


   





#SOURCES USED:
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html
#https://stackoverflow.com/questions/41513324/python-pandas-drop-rows-of-a-timeserie-based-on-time-range


# In[20]:





# In[ ]:




