#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import date


url = "http://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=advance&searchTarget=TPAM"

import time
from selenium import webdriver

# windows version
driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe')  # Optional argument, if not specified will search path.
# mac os version
# driver = webdriver.Chrome()

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

soup = BeautifulSoup(html,"lxml")
# form = soup.find_all("div",{"id":"print_area"})
form = soup.find_all("tr",{"bgcolor":"#FFFFFF"})
# title = form.find("tr",{"bgcolor":"#FFFFFF"})
# for item in form:
#     print(item.text)
print(form[0])
# print(form)


