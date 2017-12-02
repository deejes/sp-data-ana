
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import pandas as pd


# In[4]:


import seaborn as sns


# In[5]:


import numpy as np


# In[6]:


import matplotlib.pyplot as plt


# In[7]:


import time;  from datetime import datetime


# In[12]:


plt.rcParams["figure.figsize"] = (15,10)


# In[155]:


nyc = pd.read_csv('gapi_city_data-export-2017-11-30.csv')
nyc.dropna(axis=1, how='all', inplace=True) # drops all columns where all values are NaN
nyc.drop("Organic Searches", axis=1,inplace=True) # Drops Column
nyc = nyc.loc[nyc['City'] == 1023191] # Selects records only NYC


# In[157]:


weather = pd.read_csv('open_weather_6cities.csv')
weather.dropna(axis=1, how='all', inplace=True) # drops all columns where all values are NaN
weather = weather.loc[weather['city_id'] == 5128581] # Selects records only NYC


# In[158]:


def unixtimestamp(row):
    return int(int(time.mktime(datetime.strptime(row, "%Y%m%d%H").timetuple())))


# In[159]:


nyc['unix_time'] = nyc.apply(lambda row: unixtimestamp(str(row['Date Hour'])), axis=1)


# In[160]:


df = nyc.join(weather.set_index('dt'), on='unix_time')


# In[180]:


df[df['temp'].isnull()]


# In[168]:


df[["User Type",'Sessions','Transactions', 'Revenue Per User','temp']]


# In[173]:


df['weather_main'].isnull().sum()


# In[154]:


df.head()


# In[ ]:


df3['City_name'] = (df3['City']).map(find_city_name)


# In[10]:


df = df[['dt','dt_iso','temp','weather_id','weather_main']]


# In[11]:


df.loc[df['dt'] == 1498978800]


# In[42]:


df.weather_main.unique()


# In[44]:


df2 = df.pivot_table(columns='weather_main',values='dt', aggfunc='count')


# In[53]:


df2.drop(['Dust',"Sand",'Smoke',"Squall"], axis=1,inplace = True)


# In[55]:


d = df2.plot.bar()


# In[79]:


t = df['dt_iso'].iloc[25]


# In[80]:


t


# In[101]:


f = time.strptime('2015-01-01 00:00:00 +0000 UTC', "%Y-%d-%m %H:%M:%S +0000 %Z")


# In[100]:


f


# In[98]:


datetime.fromtimestamp(time.mktime(f))

