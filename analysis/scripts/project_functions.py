import pandas as pd
import numpy as np
import seaborn as sns

spy = "~/project-group23-project/data/raw/spy.csv"
tsla = "~/project-group23-project/data/raw/TSLA.csv"
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