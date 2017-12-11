#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import date


url = "http://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=advance&searchTarget=TPAM"

import time
from selenium import webdriver

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get(url);
# time.sleep(1) # Let the user actually see something!
search_box = driver.find_element_by_name('tenderName')
search_box.send_keys('智慧')
# time.sleep(1)
tenderDate = driver.find_element_by_id('rangeTenderDateRadio').click()
search_box.submit()
html = driver.page_source
# time.sleep(1) # Let the user actually see something!
driver.quit()

soup = BeautifulSoup(html)
form = soup.find_all(class = "T12b")
print(form.text)


