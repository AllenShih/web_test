#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
print("Hello World")
f = open("reporttest.csv","w", encoding = 'utf8')
w = csv.writer(f)

url = "https://data.gov.tw/datasets/search?qs=%E5%9C%B0%E4%B8%8B%E6%B0%B4"
url_base = "https://data.gov.tw"
cnt = 1
for i in range(4):
    r=requests.get(url + "&page=" + str(cnt))
    c=r.content
    soup=BeautifulSoup(c,"lxml")
    block = soup.find_all("div", {"class":"node node-dataset node-promoted node-teaser node-viewmode-teaser clearfix"})
    # for item in block:
        # print(item)
    for item in block:
        header = item.find("a")
        print(header.text)
        # url_new = url_base + header.get('href')
        # content = item.findNext("content")
        # real_content = content.findNext("")
        # data = [[header.text, url_new, real_content.text]]
        # w.writerows(data)
    cnt = cnt + 1
# print(real_content.text)