#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# name = 15
# print(type(name))

# a = 2
# print(a)
# a += 1 
# # a = a+1
# print(a)

# i = 1

# for item in range(10):
#     new_number = i+item
#     # print(new_number)

# def circle_area(radius):
#     area = radius*radius*3.14159
#     print(area)

# circle_area(6)

# result = 1
# for i in range(5):
#     result = result*(i+1)
# print(result)

def factorial(number):
    result = 1
    for i in range(number):
        result = result*(i+1)
    print(result)
a=0
while (a < 5):
    a = a+1
    factorial(a)