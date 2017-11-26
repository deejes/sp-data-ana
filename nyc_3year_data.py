
# coding: utf-8

# In[54]:


import json; import requests; import datetime; import time; import datetime; import csv


# In[99]:


date = "01/01/2016"


# In[128]:


t = str(int(time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y").timetuple())))


# In[129]:


t


# In[105]:


# set api_key
with open("dark_sky_api_key.txt", "r") as myfile:
    api_key = myfile.readlines()[0][:-1]


# In[110]:


nyc = {'lat':'42.3601','long':'71.0589'}


# In[106]:


base_url = 'https://api.darksky.net/forecast/'


# In[138]:


flags = '?exclude=currently,flags,hourly'


# In[139]:


url = "{:s}{:s}/{:s},{:s},{:s}{:s}".format(base_url,api_key,nyc['lat'], nyc['long'],str(t),flags)


# In[140]:


response = requests.get(url)


# In[141]:


json_data = json.loads(response.text)


# In[142]:


json_data


# In[145]:


with open('data.txt', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(values)


# In[72]:





# In[144]:


values = list(json_data['daily']['data'][0].values())


# In[89]:


values.append('/n')

