#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


f = open("report.csv","w", encoding = 'utf8')
w = csv.writer(f)

url = "http://wise.wra.gov.tw/dataset"
url_base = "http://wise.wra.gov.tw"
cnt = 1
for i in range(10):
    r=requests.get(url + "?page=" + str(cnt))
    c=r.content
    soup=BeautifulSoup(c,"lxml")
    block = soup.find_all("li", {"class":"dataset-item"})
    for item in block:
        header = item.find("a")
        url_new = url_base + header.get('href')
        content = item.findNext("div")
        real_content = content.findNext("div")
        data = [[header.text, url_new, real_content.text]]
        w.writerows(data)
    cnt = cnt + 1
# print(real_content.text)
    

