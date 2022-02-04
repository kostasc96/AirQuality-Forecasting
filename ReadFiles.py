import pandas as pd
import datetime
import csv
import re



def data_cleaning_temperature(temp):
    if temp < 0:
        return -1
    elif 0 <= temp <= 5:
        return 0
    elif 6 <= temp <= 10:
        return 1
    elif 11 <= temp <= 15:
        return 2
    elif 16 <= temp <= 25:
        return 3
    elif 26 <= temp <= 30:
        return 4
    elif 31 <= temp <= 40:
        return 5
    else:
        return 6


# In[4]:


def data_cleaning_winddirection(degrees):
    if 348.75 <= degrees <= 380 or 0 <= degrees <= 11.25:
        return 'N'
    elif 11.25 < degrees < 33.75:
        return 'NNE'
    elif 33.75 <= degrees <= 56.25:
        return 'NE'
    elif 56.25 < degrees < 78.75:
        return 'ENE'
    elif 78.25 <= degrees <= 101.25:
        return 'E'
    elif 101.25 < degrees < 123.75:
        return 'ESE'
    elif 123.75 <= degrees <= 146.25:
        return 'SE'
    elif 146.25 < degrees < 168.75:
        return 'SSE'
    elif 168.75 <= degrees <= 191.25:
        return 'S'
    elif 191.25 < degrees < 213.75:
        return 'SSW'
    elif 213.75 <= degrees <= 236.25:
        return 'SW'
    elif 236.25 < degrees < 258.75:
        return 'WSW'
    elif 258.75 <= degrees <= 281.25:
        return 'W'
    elif 281.25 < degrees < 303.75:
        return 'WNW'
    elif 303.75 <= degrees <= 326.25:
        return 'NW'
    else:
        return 'NNW'


# In[5]:


def data_cleaning_windspeed(speed):
    if speed < 1:
        return 0
    elif 1 <= speed < 6:
        return 1
    elif 6 <= speed < 12:
        return 2
    elif 12 <= speed < 20:
        return 3
    elif 20 <= speed < 29:
        return 4
    elif 29 <= speed < 39:
        return 5
    elif 39 <= speed < 50:
        return 6
    elif 50 <= speed < 62:
        return 7
    elif 62 <= speed < 5:
        return 8
    elif 75 <= speed < 89:
        return 9
    elif 89 <= speed < 103:
        return 10
    elif 103 <= speed < 118:
        return 11
    else:
        return 12


# In[6]:


def data_cleaning_humidity(humidity):
    if humidity < 25:
        return 0
    elif 25 <= humidity < 30:
        return 1
    elif 30 <= humidity <= 60:
        return 2
    elif 60 <= humidity < 70:
        return 3
    else:
        return 4


# In[21]:


def weather_df(dataset_weather, output, file_format, file_path):
    tmp = 0
    dataset_weather = file_path + dataset_weather + '.' + file_format
    #dataset_forecast = file_path + dataset_forecast + '.' + file_format
    weather = pd.read_csv(dataset_weather, sep=',')
    #forecast = pd.read_csv(dataset_forecast, sep=',')
    weather = weather.rename(columns={"time":"date_time","temp": "real_temp", "rhum":"real_humidity","wdir":"real_winddir","wspd":"real_windspd"})
    weather['temp_dir'] = ""
    weather = weather[['date_time','real_temp','real_humidity','real_winddir','real_windspd','temp_dir']]
    for i, row in weather.iterrows():
        weather.at[i, 'date_time'] = weather.date_time
        
        if weather.at[i,'real_temp'] is None and i > 0:
            weather.at[i,'real_temp'] = weather.iloc[[tmp]].forecast_tempC
        else:
            weather.at[i,'real_temp'] = data_cleaning_temperature(row.real_temp)
        
        if weather.at[i,'real_humidity'] is None and i > 0:
            weather.at[i,'real_humidity'] = weather.iloc[[tmp]].forecast_humidity
        else:
            weather.at[i,'real_humidity'] = data_cleaning_humidity(row.real_humidity)
        
        if weather.at[i,'real_winddir'] is None and i > 0:
            weather.at[i,'temp_dir'] = weather.iloc[[tmp]].forecast_windDirection
        else:
            weather.at[i,'temp_dir'] = data_cleaning_winddirection(row.real_winddir)
        
        if weather.at[i,'real_windspd'] is None and i > 0:
            weather.at[i,'real_windspd'] = weather.iloc[[tmp]].forecast_windSpeed
        else:
            weather.at[i,'real_windspd'] = data_cleaning_windspeed(row.real_windspd)
        
        tmp = i
    
    weather = weather.drop(columns=['real_winddir'])
    weather = weather.rename(columns={"temp_dir":"real_winddir"})
    weather.to_csv('CleanFiles/' + output + '.csv')


weather_df('PireusWeather', 'PireusClean','csv', 'CleanFiles/')