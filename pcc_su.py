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


def send_gmail(top_priority):
    smtpserver = "smtp.gmail.com"
    login = "clshih73@gmail.com"
    password = "workaccount1234"
    sender = "clshih73@gmail.com"
    receivers = ["kingjames1324@gmail.com","ericsu0913@gmail.com","alex332233@gmail.com"]
    # receivers = ["kingjames1324@gmail.com"]
    date = datetime.date.today()
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = ", ".join(receivers)
    msg["Subject"] = "電子採購網搜尋結果(標的：智慧、大數據、物聯網、水資源) "+str(date)
# <td>"+str(item[6])+"</td>\
    Text = "<html><p><b>電子採購網自動搜尋</b><p><html>\n"
    # Text = Text + "<p>Criteria : 金額大於三百萬、關鍵字出現次數大於二</p>"
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
    for item in top_priority:
        Text = Text + "<tr>\
        　              <td>"+item[0]+"</td>\
        　              <td>"+item[1]+"</td>\
                        <td>"+item[2]+"</td>\
                        <td>"+item[3]+"</td>\
                        <td>"+item[4]+"</td>\
                        <td>"+item[5]+"</td>\
                        <td>"+"<a href="+item[6]+">URL</a>"+"</td>\
        　               </tr>"
    Text = Text +"</table>\n"
    # Text = Text +"<p><b>其餘完整搜尋結果於附件</b></p>"

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


# windows version
# driver = webdriver.Chrome(executable_path=r'C:/Webdrivers/chromedriver.exe')  # Optional argument, if not specified will search path.
# mac os version
driver = webdriver.Chrome()

driver.get(url)
# time.sleep(1) # Let the user actually see something!
Ａ = ["水庫","地下水","防汛","灌溉","節水","管理模式","水管理","自來水","水網","雨水","用水","水資源物聯網","水源","河川"]
key_words = [A]
all_key_words = A
html_all = []

# open up the browser and do the search
for item in key_words:
    html_container = []
    for words in item:
        search_box = driver.find_element_by_name('tenderName')
        search_box.clear() # clear the search box
        search_box.send_keys(words) # enter the word in search box
        tenderDate = driver.find_element_by_id('rangeTenderDateRadio').click() #click on the right box
        # time.sleep(1)
        search_box.submit() #送出
        html = driver.page_source 
        time.sleep(1) # Let the user actually see something!
        driver.back() #上一頁
        # html_container.append([html, words])
        # html_all.append([html, words])
        html_container.append([html, words])
    html_all.append(html_container)
driver.quit()


base_url = "http://web.pcc.gov.tw/tps"
top_priority = []
top_priority_title = []
# label = ["A_slopeland","B_smart","C_resource","D_land"]
# cnt = 0
for html_set in html_all:
    # file_name = label[cnt]+".csv"
    # f = open(file_name,"w", encoding = 'utf_8_sig')
    # f.write(codecs.BOM_UTF8)
    # w = csv.writer(f)
    # top_row = [["分類","機關名稱","標案名稱","傳輸次數","公告日期","截止日期","金額","網址"]]
    # w.writerows(top_row)
    for data in html_set:
        soup = BeautifulSoup(data[0],"lxml")
        # form = soup.find_all("div",{"id":"print_area"})
        form1 = soup.find_all("tr",{"bgcolor":"#FFFFFF"})
        form2 = soup.find_all("tr",{"bgcolor":"#D6FAC5"})
        keywords = data[1]

        for item in form1 :
            num = item.findNext('td')
            facility = num.findNext('td')
            title_old = facility.findNext('td')
            if title_old.find('a') != None:
                title = title_old.find('a').text
                temp_cnt = 0
                for word in all_key_words:
                    if word in title:
                        temp_cnt+=1
                url_lat = item.find('a').get('href')
                url_all = base_url+url_lat[2:]
                times = title_old.findNext('td')
                tenderway = times.findNext('td')
                category = tenderway.findNext('td')
                start_date = category.findNext('td')
                end_date = start_date.findNext('td')
                money = end_date.findNext('td')
                new_money = money.text.strip().replace(",","")  
                if new_money != "" and int(new_money)>=0 and temp_cnt >= 0:
                    if title not in top_priority_title:
                        temp_list = [keywords, facility.text.strip(), title.strip(), times.text,\
                        money.text.strip(), end_date.text.strip(), url_all.strip()]
                        top_priority.append(temp_list)
                        top_priority_title.append(title)
                # if new_money != "" and int(new_money)>2000000 and category.text == "勞務類" and tenderway.text != "公開取得報價單或企劃書":
                #     data = [[keywords, facility.text.strip(), title.strip(), int(times.text),\
                #     start_date.text.strip(), end_date.text.strip(), money.text,\
                #     url_all.strip()]]
                #     w.writerows(data)
            # print(data)

        for item in form2 :
            num = item.findNext('td')
            facility = num.findNext('td')
            title_old = facility.findNext('td')
            if title_old.find('a') != None:
                title = title_old.find('a').text
                temp_cnt = 0
                for word in all_key_words:
                    if word in title:
                        temp_cnt+=1
                url_lat = item.find('a').get('href')
                url_all = base_url+url_lat[2:]
                times = title_old.findNext('td')
                tenderway = times.findNext('td')
                category = tenderway.findNext('td')
                start_date = category.findNext('td')
                end_date = start_date.findNext('td')
                money = end_date.findNext('td')
                new_money = money.text.strip().replace(",","")  
                if new_money != "" and int(new_money)>=0 and temp_cnt >= 0:
                    if title not in top_priority_title:
                        temp_list = [keywords, facility.text.strip(), title.strip(), times.text,\
                        money.text.strip(), end_date.text.strip(), url_all.strip()]
                        top_priority.append(temp_list)
                        top_priority_title.append(title)
                # if new_money != "" and int(new_money)>2000000 and category.text == "勞務類" and tenderway.text != "公開取得報價單或企劃書":
                #     data = [[keywords, facility.text.strip(), title.strip(), int(times.text),\
                #     start_date.text.strip(), end_date.text.strip(), money.text,\
                #     url_all.strip()]]
                #     w.writerows(data)
            # print(data)
    # cnt += 1
    # f.close()

# print(top_priority)
send_gmail(top_priority)