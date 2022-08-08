#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


Location = r'dataframe.csv'
d = pd.read_csv(Location)
df = pd.DataFrame(d)
df.drop(df.columns[[10, 11,20]], axis=1,inplace=True)
df



# In[16]:


Location = r'isochrone.csv'
d = pd.read_csv(Location,index_col=0)
df1 = pd.DataFrame(d)

df1

