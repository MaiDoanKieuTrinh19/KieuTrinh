# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:25:00 2024

@author: MaiDoanKieuTrinh-23732851
"""
import math
N=int(input('Nhập vào số nguyên dương có 2 chữ số N= '))
if 10<=N<=99:
    x=N//10
    y=N%10
    a=x+y
    print('Tổng các chữ số của N là: ', a)
else:
    print('Vui lòng nhập số nguyên có 2 chữ số')
 
 