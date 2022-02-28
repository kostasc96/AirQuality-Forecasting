#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime
import csv


# In[3]:


my_dict = {}

def weather_df(dataset_weather, output, file_format, file_path):
    tmp_temp = None 
    tmp_humidity = None 
    tmp_winddir = None 
    tmp_windspd = None 
    tmp_pm10 = -9999.0
    dataset_weather = file_path + dataset_weather + '.' + file_format
    weather = pd.read_csv(dataset_weather, sep=',')
    for i, row in weather.iterrows():
        if weather.at[i,'pm10'] ==  -9999.0 and i > 0:
            if my_dict[weather.at[i,'date_time'][11:13]]:
                weather.at[i,'pm10'] = weather.at[i,'date_time'][11:13]
            else:
                weather.at[i,'pm10'] = tmp_pm10
        else:
            tmp_pm10 = weather.at[i,'pm10']
            my_dict[weather.at[i,'date_time'][11:13]] = tmp_pm10
        tmp = i
    
    weather.to_csv('CleanFiles/' + output + '.csv')


# In[4]:


weather_df('NeaSmirni','NeaSmirni','csv','CleanFiles/')

weather_df('AgiaParaskevi','AgiaParaskevi','csv','CleanFiles/')
weather_df('Aristotelous','Aristotelous','csv','CleanFiles/')
weather_df('Athens','Athens','csv','CleanFiles/')
weather_df('Elefsina','Elefsina','csv','CleanFiles/')

weather_df('Koropi','Koropi','csv','CleanFiles/')
weather_df('Liosia','Liosia','csv','CleanFiles/')
weather_df('Lykovrisi','Lykovrisi','csv','CleanFiles/')
weather_df('Marousi','Marousi','csv','CleanFiles/')

weather_df('Patision','Patision','csv','CleanFiles/')
weather_df('Peristeri','Peristeri','csv','CleanFiles/')
weather_df('Pireus','Pireus','csv','CleanFiles/')
weather_df('Thrakomakedones','Thrakomakedones','csv','CleanFiles/')

