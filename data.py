#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

# data = pd.read_csv("data.csv")
# print(data)


road =[]
with open("data.csv", encoding = 'utf8') as w:
    content = w.readlines()
    for lines in content:
        split_line = lines.split(",")
        print(split_line)