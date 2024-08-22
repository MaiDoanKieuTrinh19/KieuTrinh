# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:38:02 2024

@author: MaiDoanKieuTrinh-23732851
"""
import math
a=float(input('Nhap gia tri cua a: '))
b=float(input('Nhap gia tri cua b: '))
A= (math.sqrt(a) - math.sqrt(b)) / (math.pow(a,0.25) - math.pow(b,0.25))
B= (math.sqrt(a) + math.pow(a*b,0.25)) / (math.pow(a,0.25) + math.pow(b,0.25))
C= A-B
print('Ket qua la: ',round(C,3))

