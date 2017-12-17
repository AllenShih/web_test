#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = "http://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=advance&searchTarget=TPAM"

def encode_decode(self):
    self = self.encode("utf8").decode("cp950", "ignore")
    # self = self.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
    return self

# windows version
# driver = webdriver.Chrome(executable_path=r'C:/Webdrivers/chromedriver.exe')  # Optional argument, if not specified will search path.
# mac os version
driver = webdriver.Chrome()

driver.get(url)
# time.sleep(1) # Let the user actually see something!
A = ["坡地","邊坡","崩塌","土石流","防災","土砂"]
B = ["智慧","大數據","物聯網","雲端"]
C = ["水資源","太陽能","綠能"]
D = ["社區","土地利用","土地可利用"]
key_words = [A,B,C,D]
html_all = []

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
# for item in html_all:
#     print(item)

base_url = "http://web.pcc.gov.tw/tps"

label = ["A_坡地","B_智慧","C_資源","D_土地"]
cnt = 0
for html_set in html_all:
    file_name = label[cnt]+".csv"
    f = open(file_name,"w", encoding = 'utf8')
    w = csv.writer(f)
    top_row = [["分類","機關名稱","標案名稱","傳輸次數","公告日期","截止日期","金額","網址"]]
    w.writerows(top_row)

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
            title = title_old.find('a').text
            url_lat = item.find('a').get('href')
            url_all = base_url+url_lat[2:]
            times = title_old.findNext('td')
            tenderway = times.findNext('td')
            category = tenderway.findNext('td')
            start_date = category.findNext('td')
            end_date = start_date.findNext('td')
            money = end_date.findNext('td')
            data = [[keywords, facility.text.strip(), title.strip(), int(times.text),\
            start_date.text.strip(), end_date.text.strip(), money.text.strip(),\
            url_all.strip()]]
            w.writerows(data)
            # print(data)

        for item in form2 :
            num = item.findNext('td')
            facility = num.findNext('td')
            title_old = facility.findNext('td')
            title = title_old.find('a').text
            url_lat = item.find('a').get('href')
            url_all = base_url+url_lat[2:]
            times = title_old.findNext('td')
            tenderway = times.findNext('td')
            category = tenderway.findNext('td')
            start_date = category.findNext('td')
            end_date = start_date.findNext('td')
            money = end_date.findNext('td')
            data = [[keywords, facility.text.strip(), title.strip(), int(times.text),\
            start_date.text.strip(), end_date.text.strip(), money.text.strip(),\
            url_all.strip()]]
            # data = [[title.strip()]]
            w.writerows(data)
            # print(data)
    cnt += 1
    f.close()
