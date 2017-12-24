#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime, math, time
# import pyodbc
from pathlib import Path
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import os
# from apscheduler.schedulers.blocking import BlockingScheduler

# date = "2017-10-11 00:00:55.000"
# date2 = "2017-10-11 00:00:55.000"
# now = datetime.datetime.now() #.strftime('%Y-%m-%d %H:%M:%S')
<<<<<<< HEAD
# # print(now)
# delta = datetime.date(2017, 12, 31)-now.date()
# # print(delta.days)
# for i in range(4):
#     print(i)
smtpserver = "smtp.gmail.com"
login = "clshih73@gmail.com"
password = "As34710125"
sender = "clshih73@gmail.com"
receivers = ["kingjames1324@gmail.com"]

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = ", ".join(receivers)
msg["Subject"] = "Test Message"

Text = "<html><p>電子採購網自動搜尋<p><html>\n"
Text = Text + "<table>\
　               <tr>\
　               <td style="color: red;">分類</td>\
　               <td>機關</td>\
                 <td>案名</td>\
                 <td>次數</td>\
                 <td>金額</td>\
                 <td>截止日期</td>\
                 <td>Link</td>\
　               </tr>\
　               <tr>\
　               <td>坡地</td>\
　               <td>行政院農業委員會水土保持局</td>\
                 <td>107年度山坡地開發防災設計標準提升及水土保持技術規範法規檢討</td>\
                 <td>1</td>\
                 <td>3300000</td>\
                 <td>106/12/26</td>\
                 <td>http://web.pcc.gov.tw/tps/tpam/main/tps/tpam/tpam_tender_detail.do?searchMode=common&scope=F&primaryKey=52372138</td>\
　               </tr>\
                </table>"

msg.attach(MIMEText(Text,'html','utf-8'))
filenames = ["A_slopeland.csv","B_smart.csv","C_resource.csv","D_land.csv"]
# filenames = ["A_slopeland.csv",]

for file in filenames:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(open(file,'rb').read())
    encode_base64(part)
    part.add_header("Content-Disposition", 'attachment; filename="%s"' % os.path.basename(file))
    msg.attach(part)


smtpObj = smtplib.SMTP()
smtpObj.connect(smtpserver,25)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.ehlo()
smtpObj.login(login,password)
smtpObj.sendmail(sender,receivers,msg.as_string())
smtpObj.quit()


# import sys
# # reload(sys)
# sys.setdefaultencoding('utf8')
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.header import Header
 
# #發送郵件服務器
# smtpserver = 'smtp.gmail.com'
# #發送郵箱用户名和密碼
# user = 'clshih73@gmail.com'
# password = 'As34710125'
# #發送郵箱
# sender = 'clshih73@gmail.com'
# #接受郵箱
# receiver = 'kingjames1324@gmail.com'
 
# #創建一個帶附件的實例
# message = MIMEMultipart()
# message['From'] = Header('Python 測試','utf-8')
# message['To'] = Header('測試','utf-8')
# subject = 'Python SMTP郵件測試'
# message['Subject'] = Header(subject,'utf-8')

# #郵件正文內容
# message.attach(MIMEText('這是測試Python發送附件功能....','plain','utf-8'))

# #構造附件1，傳送當前目錄下的test.txt文檔
# att1 = MIMEText(open('test.txt','rb').read(),'base64','utf-8')
# att1['Content-Type'] = 'application/octet-stream'
# #這裏的filename可以任意寫，寫什幺名字 郵件中就顯示什幺名字
# att1['Content-Disposition'] = 'attachment;filename:"123.txt"'
# message.attach(att1)

# smtp = smtplib.SMTP()
# smtp.connect(smtpserver,25)
# smtp.ehlo()
# smtp.starttls()
# smtp.ehlo()
# smtp.login(user,password)
# smtp.sendmail(sender,receiver,message.as_string())
# smtp.quit()
=======
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
>>>>>>> a60af0a2d4b8726a552333e2502e9a54dc2f41ec
