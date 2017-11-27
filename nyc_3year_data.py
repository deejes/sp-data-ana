
# coding: utf-8

# In[6]:


import json; import requests; import datetime; import time; import datetime; import csv


# In[92]:


def date_string_to_unix(date_string):
    return (str(int(time.mktime(datetime.datetime.strptime(date_string, "%d/%m/%Y").timetuple()))))


# In[118]:


from datetime import date, timedelta

d1 = date(2016, 1, 1)  # start date
d2 = date(2016, 12, 31)  # end date

delta = d2 - d1         # timedelta

dates = [(d1 + datetime.timedelta(days=i)) for i in range(delta.days + 1)]
dates = [x.strftime('%d/%m/%Y') for x in dates]


# In[115]:


unix_dates  = [date_string_to_unix(dates[x]) for x in range(len(dates))]


# In[119]:


unix_dates


# In[126]:


# set api_key
with open("dark_sky_api_key.txt", "r") as myfile:
    api_key = myfile.readlines()[0][:-1]


# In[127]:


nyc = {'lat':'42.3601','long':'71.0589'}


# In[128]:


base_url = 'https://api.darksky.net/forecast/'


# In[159]:


flags = '?exclude=currently,flags,hourly'


# In[170]:


units = '&units=si'


# In[171]:


url = "{:s}{:s}/{:s},{:s},{:s}{:s}{:s}".format(base_url,api_key,nyc['lat'], nyc['long'],unix_dates[0],flags,units)


# In[172]:


response = requests.get(url)


# In[173]:


(response.text)


# In[174]:


json_data = json.loads(response.text)


# In[175]:


json_data


# In[182]:


with open('data.txt', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(keys)


# In[183]:


with open('data.txt', 'a') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(values)


# In[178]:


values = list(json_data['daily']['data'][0].values())


# In[179]:


values.append('/n')


# In[180]:


keys = list(json_data['daily']['data'][0].keys())

