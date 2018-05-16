#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import random

cal_15 = open("cal_15.csv", "r")
f = open("output.csv","w",newline = "")
w = csv.writer(f)
# and cnt <= 490
factors = csv.reader(cal_15)
cnt = 0
for row in factors:
    if (len(row[0]) == 7 and cnt <= 1500):
        cnt = cnt + 1 
        new_row = []
        new_row.append(0)
        for item in row[0]:
            new_row.append(item)
        new_row.append("No")
        w.writerow(new_row)
    if (len(row[0]) == 9):
        new_row = []
        first_digit = row[0][0]
        print(first_digit)
        row[0] = row[0][1:]
        for item in row[0]:
            new_row.append(item)
        new_row.append("Yes")
        w.writerow(new_row)
    if (len(row[0]) == 8 and cnt <= 1500):
        cnt = cnt + 1
        new_row = []
        for item in row[0]:
            new_row.append(item)
        new_row.append("No")
        w.writerow(new_row)
# print(random.randint(0, 100, 3))