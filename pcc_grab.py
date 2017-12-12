#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup
from datetime import date


url = "http://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=advance&searchTarget=TPAM"

import time
from selenium import webdriver

# windows version
# driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe')  # Optional argument, if not specified will search path.
# mac os version
driver = webdriver.Chrome()

driver.get(url);
# time.sleep(1) # Let the user actually see something!
search_box = driver.find_element_by_name('tenderName')
search_box.send_keys('智慧')
# time.sleep(1)
tenderDate = driver.find_element_by_id('rangeTenderDateRadio').click()
search_box.submit()
html = driver.page_source
# time.sleep(5) # Let the user actually see something!
driver.quit()

f = open("tender.csv","w")
w = csv.writer(f)
top_row = [["項次","機關名稱","標案名稱","網址","次數","招標方式","標的分類","公告日期","截止日期"]]
w.writerows(top_row)

soup = BeautifulSoup(html,"lxml")
# form = soup.find_all("div",{"id":"print_area"})
form1 = soup.find_all("tr",{"bgcolor":"#FFFFFF"})
form2 = soup.find_all("tr",{"bgcolor":"#D6FAC5"})

base_url = "http://web.pcc.gov.tw/tps"


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
    data = [[num.text, facility.text.strip(), title.strip(), url_all.strip(), times.text.strip(), tenderway.text, category.text, start_date.text, end_date.text]]
    w.writerows(data)

for item in form2:
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
    data = [[num.text, facility.text, title, url_all, times.text.strip(), tenderway.text, category.text, start_date.text, end_date.text]]
    w.writerows(data)


f.close()
