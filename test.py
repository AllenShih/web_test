#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime, math, time
# import pyodbc
from pathlib import Path
# from apscheduler.schedulers.blocking import BlockingScheduler

# date = "2017-10-11 00:00:55.000"
# date2 = "2017-10-11 00:00:55.000"
# now = datetime.datetime.now() #.strftime('%Y-%m-%d %H:%M:%S')
# dt = datetime.datetime(2017, 12, 18, 12, 30, 59, 0)
# timed = datetime.timedelta(hours=-5)
# delta = dt-datetime.datetime.now()
# print(delta)
# print(dt)
# print(datetime.datetime.now())
# print(dt<datetime.datetime.now())
# print(6*timed)

# array = [0,1,2,3,4]
# print(array)
# array.pop()
# print(array)
# new_array = array[1:]
# print(new_array)

dt1 = datetime.datetime(2017, 12, 18, 12, 30, 59, 0)
dt2 = datetime.datetime(2017, 12, 19, 12, 30, 59, 0)
dt3 = datetime.datetime(2017, 12, 20, 12, 30, 59, 0)
dt4 = datetime.datetime(2017, 12, 21, 12, 30, 59, 0)
dt5 = datetime.datetime(2017, 12, 20, 12, 00, 59, 0)
dt6 = datetime.datetime(2017, 12, 19, 12, 00, 59, 0)
arr = []
timedelta = datetime.timedelta(hours=6)
if (dt3 - timedelta) > dt6:
    print("success")
else:
    print("failed")


arr.append([0,dt1])
arr.append([1,dt2])
arr.append([2,dt3])
arr.append([3,dt4])
# for item in arr:
#     arr.remove(item)
#     print(arr)
print((dt4-dt1).days)
arr = [x for x in arr if x[1]<dt5 and x[1]>dt6]
print(arr)
# print(arr.remove([0,dt1]))
# print(arr)
# def array_remover(array, remove):
#     array.remove(remove)

# arra = ["0","1","2","3","4","5"]
# arra = [0,1,2,3,4,5]
# # for item in arra:
    
# #     arra.remove(num)
# #     print(arra)


# arra = [x for x in arra if x > 2]
# print(arra)