#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv


f = open("水聯盟資料清單 - 水太少.csv", "r")
all_row = []
for row in f:
    e_row = []
    new_row = row.split(",")
    for item in new_row:
        e_row.append(item)
    all_row.append(e_row)

# Text = "<html><p><b>水聯盟資料清單 水太多</b><p><html>\n"
    # Text = Text + "<p>新增國家災害防救科技中心於機關分類</p>"
cnt = 0
Text = "<tr>"
for item in all_row:
    if cnt > 0:
        Text = Text + " <td>"+"<b>"+item[0]+"</b>"+"</td>\
                        <td>"+"<b>"+item[2]+"</b>"+"</td>\
                        <td>"+"<a href="+item[5]+">URL</a>"+"</td>\
                        <td>"+"<a href="+item[6]+">API</a>"+"</td>\
            　           </tr>"
    else:
        Text = Text + " <td>"+"<b>"+item[0]+"</b>"+"</td>\
                        <td>"+"<b>"+item[2]+"</b>"+"</td>\
                        <td>"+"<b>"+"URL"+"</b>"+"</td>\
                        <td>"+"<b>"+"API"+"</b>"+"</td>\
            　           </tr>"
    cnt += 1
# Text = Text +"</tbody>\n"



Html_file= open("forum.html","w")
Html_file.write(Text)
Html_file.close()