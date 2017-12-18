#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime, math, time
# import pyodbc
from pathlib import Path
# from apscheduler.schedulers.blocking import BlockingScheduler

date = "2017-10-11 00:00:55.000"
date2 = "2017-10-11 00:00:55.000"
now = datetime.datetime.now() #.strftime('%Y-%m-%d %H:%M:%S')
dt = datetime.datetime(2017, 12, 18, 12, 30, 59, 0)
timed = datetime.timedelta(hours=-5)
delta = dt-datetime.datetime.now()
print(delta)
print(dt)
print(datetime.datetime.now())
print(dt<datetime.datetime.now())
print(6*timed)

for i in range(4):
    print(i)
# money = "27,909,000"
# money = money.replace(',','')
# print(int(money))


# def get_sql():
#     # fw_log = open(log_file,'a')
#     now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     # fw_log.write('now = '+now)
#     # Connect MSSQL
#     # fw_log.write('MSSQL connect...')
#     conn = pyodbc.connect(connStr)
#     cur = conn.cursor()
#     # Get record    
#     filePath = 'C://Inetpub//wwwroot//abri//sensor//taipeicity.csv'
#     fout = open(filePath,'wt')
#     for i in range(0,len(sensorID)):
#         fw_log.write('Get [sid_'+sensorID[i]+'] record...')
#         s_id = sensorID[i]
#         record_str = ''
#         record = cur.execute("select * from "+sensorDataTable[i]+" where s_id like '%"+s_id+"%' and (rec_time between '"+StartTime+"' and '"+EndTime+"') order by rec_time")
#         filePath = 'C://Inetpub//wwwroot//abri//sensor//sid_'+str(s_id)+'.csv'
#         fout_sid = open(filePath,'wt')
#         if sensorType[i]==1:
#             fout_sid.write('rec_time,s_id,w1,w2,w3,w4,dist,v\n')
#             [record_str,last_record] = record_Commercial(s_id,record)
#         elif sensorType[i]==2:
#             fout_sid.write('rec_time,s_id,w1,w2,w3,w4,st1,st2,st3,st4,at,rh,ap,rf,inx,iny,ax,ay,az,gx,gy,gz\n')
#             [record_str,last_record] = record_SmartStick(s_id,record)
#         elif sensorType[i]==3:
#             fout_sid.write('rec_time,s_id,inx,iny\n')
#             [record_str,last_record] = record_TiltStick(s_id,record)
#         elif sensorType[i]==4:
#             # 
#             fout_sid.write('rec_time,s_id,rainfall_10m,rainfall_acc,v\n')
#             # 
#             [record_str,last_record] = record_CommercialRF(s_id,record)
            
#         fout_sid.write(record_str)
#         fout.write(last_record)
#         fout_sid.close()
#     fout.close()
#     cur.close()
#     conn.close()
#     fw_log.write('['+now+'] CSV upload done !!!\n')
#     fw_log.close()