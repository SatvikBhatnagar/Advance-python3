# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 01:59:37 2022

@author: satvik
"""

#if
a = 2
if a < 5:
    print('a < 5')
else:
    print('a >= 5')

#nested if
b = 10
if b < 5:
   print('b < 5')
else:
    if b < 10:
        print('5 <= b < 10')
    else:
        print('b >= 10')

c = 5

if c < 5:
    print('c < 5')
elif c < 10:
    print('5 <= c < 10')
elif c < 15:
    print('10 <= c < 15')
elif c < 20:
    print('15 <= c < 20')
else:
    print('c > 20')

# X if (condition is true) else Y
d = 25

if d < 5:
    e = 'd < 5'
else:
    e = 'd >= 5'
print(e)

e = 'd < 5' if d < 5 else 'd >= 5'
print(e)

