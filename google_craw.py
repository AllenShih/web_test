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
import simplejson  
def encode_decode(self):
    self = self.encode("utf8").decode("gbk", "ignore")
    # self = self.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
    return self

f = open("google_craw.csv","w", encoding = 'utf8')
w = csv.writer(f)

question = "防災+食品+公司"

url_base = "https://www.google.com.tw/search?q="
url = url_base+question

r = requests.get(url)
c = r.content
soup=BeautifulSoup(c,"lxml")
block = soup.find_all("h3", {"class":"r"})

for item in block:
    title = item.find("a")
    url_new = title.get("href") 
    print(encode_decode(title.text))
    data = [[title.text]]
    w.writerows(data)


