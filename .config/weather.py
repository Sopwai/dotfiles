#!/bin/python
# -*- coding: utf-8 -*-
# this is using python 3.6
import urllib.request, json

#input your info
city = ""                                  #put your city here
api_key = ""                              #get an api key from openweathermap
units = ""                                  #Metric or Imperial units
unit_key = ""                              #F C or K, i think kelvin is available

weather = eval(str(urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units={}".format(city, api_key, units)).read())[2:-1])

info = weather["weather"][0]["description"].capitalize()
temp = int(float(weather["main"]["temp"]))

print("%s, %i °%s" % (info, temp, unit_key))
