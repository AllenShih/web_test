#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
http://twweatherapi.appspot.com/forecast?location=12&output=json
"""
from urllib.request import urlopen
import pprint
import requests

def getweather(id):
    result=''
    url='https://data.wra.gov.tw/Service/OpenData.aspx?format=json&amp=&id=AD99E410-8E27-4B5A-AC46-143F7B74C318'
    req=urlopen(url)
    #print req.read()
    chiadict=eval(req.read())
    #print chiadict
    #print chiadict['result'] 
    pprint.pprint(chiadict['GroundHeight'])
    #print '氣象預報'
    #print "="*20
    # result=result+chiadict['result']['locationName']+' 天氣\n'
    # result+="="*10
    # result+="\n"
    # for d in chiadict['result']['items']:
    #     result+=''+d['title']+'\n'
    #     result+='時間 '+d['time']+'\n'
    #     result+='天氣狀況 '+d['description']+'\n'
    #     result+='溫度 '+d['temperature']+' 度'+'\n'
    #     result+='降雨機率 '+d['rain']+' %\n'
    #     result+='-'*10
    #     result+="\n"
    # return result
    return chiadict

# print(getweather('12'))
getweather('11')