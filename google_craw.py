#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import datetime
import os
import smtplib
import codecs

import urllib  
# import simplejson  
def encode_decode(self):
    self = self.encode("utf8").decode("gbk", "ignore")
    # self = self.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
    return self

f = open("google_craw.csv","w", encoding = 'utf8')
w = csv.writer(f)

question = "防災+食品+公司"
# question = "NBA"

url_base = "https://www.google.com/search?q="
url = url_base+question

r = requests.get(url)
c = r.content
# print(r.text)
# soup=BeautifulSoup(c,"html.parser")
soup = BeautifulSoup(c, "lxml", from_encoding="big5")

# soup=BeautifulSoup(c,"lxml")
block = soup.find_all("div", {"class":"g"})

base_url = "https://www.google.com.tw"
page_tag = soup.find_all("a", {"class":"fl"})
for item in page_tag:
    page_url = item.get("href") 
    
    print(base_url + page_url)

for item in block:
    title = item.find("a")
    # url_new = title.get("href") 
    url_new = item.find('cite')
    # print(encode_decode(title.text)){"class":"_Rm"}
    print(title.text)
    print(url_new.text)
    data = [[title.text, url_new.text]]
    w.writerows(data)




