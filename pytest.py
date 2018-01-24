#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import datetime
import os
import smtplib
import codecs
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.encoders import encode_base64

# url = "http://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=advance&searchTarget=TPAM"
url = "http://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=basic"
def encode_decode(self):
    self = self.encode("utf8").decode("cp950", "ignore")
    # self = self.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
    return self


def send_gmail():
    smtpserver = "smtp.gmail.com"
    login = "clshih73@gmail.com"
    password = "workaccount1234"
    sender = "clshih73@gmail.com"
    # receivers = ["kingjames1324@gmail.com", "cwshen@sinotech.org.tw", "pcchi@sinotech.org.tw"," ywlin@sinotech.org.tw",\
    # "tyt1006@sinotech.org.tw","lschou@sinotech.org.tw","baconlin@sinotech.org.tw","khlin0506@gmail.com"]
    # receivers = ["kingjames1324@gmail.com","khlin0506@gmail.com"]
    receivers = ["kingjames1324@gmail.com"]
    date = datetime.date.today()
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = ", ".join(receivers)
    msg["Subject"] = "電子採購網搜尋結果 "+str(date)
# <td>"+str(item[6])+"</td>\
    Text = "<html><p><b>電子採購網自動搜尋</b><p><html>\n"
    Text = Text + "<p>Criteria : 金額大於三百萬、關鍵字出現次數大於二</p>"
    Text = Text + " <table>\
    　               <tr>\
    　               <td>"+"<b>"+"分類"+"</b>"+"</td>\
    　               <td>"+"<b>"+"機關"+"</b>"+"</td>\
                     <td>"+"<b>"+"案名"+"</b>"+"</td>\
                     <td>"+"<b>"+"次數"+"</b>"+"</td>\
                     <td>"+"<b>"+"金額"+"</b>"+"</td>\
                     <td>"+"<b>"+"截止日期"+"</b>"+"</td>\
                     <td>"+"<b>"+"Link"+"</b>"+"</td>\
    　               </tr>"
    # for item in top_priority:
    #     Text = Text + "<tr>\
    #     　              <td>"+item[0]+"</td>\
    #     　              <td>"+item[1]+"</td>\
    #                     <td>"+item[2]+"</td>\
    #                     <td>"+item[3]+"</td>\
    #                     <td>"+item[4]+"</td>\
    #                     <td>"+item[5]+"</td>\
    #                     <td>"+"<a href="+item[6]+">URL</a>"+"</td>\
    #     　               </tr>"
    Text = Text +"</table>\n"
    Text = Text +"<p><b>其餘完整搜尋結果於附件</b></p>"

    msg.attach(MIMEText(Text,'html','utf-8'))
    # filenames = ["A_slopeland.csv","B_smart.csv","C_resource.csv","D_land.csv"]

    # for file in filenames:
    #     part = MIMEBase("application", "octet-stream")
    #     part.set_payload(open(file,'rb').read())
    #     encode_base64(part)
    #     part.add_header("Content-Disposition", 'attachment; filename="%s"' % os.path.basename(file))
    #     msg.attach(part)
    smtpObj = smtplib.SMTP()
    smtpObj.connect(smtpserver,587)
    smtpObj._host = "smtp.gmail.com"
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.ehlo()
    smtpObj.login(login,password)
    smtpObj.sendmail(sender,receivers,msg.as_string())
    smtpObj.quit()




send_gmail()