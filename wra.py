#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

url = "https://www.cp.gov.tw/portal/Clogin.aspx?returnurl=https%3a%2f%2fdata.wra.gov.tw%2fSSOLogin.aspx&level=1"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)
account = driver.find_element_by_name('ctl00$ContentPlaceHolder1$AccountPassword1$txt_account')
account.clear()
account.send_keys("ciaoshih")
time.sleep(1)
password = driver.find_element_by_name('ctl00$ContentPlaceHolder1$AccountPassword1$txt_password')
password.clear()
password.send_keys("qaz54321")
time.sleep(1)
login = driver.find_element_by_name("ctl00$ContentPlaceHolder1$AccountPassword1$btn_LoginHandler")
login.click()
time.sleep(5)
enter_app = driver.find_element_by_id("ctl00_ContentPlaceHolder1_lViewData_ctrl0_hLinkGoto")
enter_app.click()

