# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 05:50:47 2022

@author: satvik
"""

#The For Loop

''' In Python, an iterable is an object capable of returning values one at a time. '''
i = 0
while i < 5:
    print(i)
    i += 1
i = None
print('-----------------------')

#writing the same code with FOR LOOP

for i in range(5):
    print(i)

print('-----------------------')

for c in 'hello':
    print(c)

print('-----------------------')

for x in ('a', 'b', 'c', 4):
    print(x)

print('-----------------------')

for x in [(1, 2), (3, 4), (5, 6)]:
    print(x)

print('-----------------------')

for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)

print('-----------------------')

for i in range(5):
    if i == 3:
        continue
    print(i)

print('-----------------------')

for i in range(5):
    if i == 3:
        break
    print(i)

print('-----------------------')

for i in range(1, 5):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break
else: #this is again something very interesting, the else is working with the
        #previous IF but one level out of it!
    print('no multiples of 7 in the range')

print('-----------------------')

for i in range(5):
    print('#######')
    try:
        10 / (i-3)
    except ZeroDivisionError:
        print('divided by 0')
        continue
    finally:
        print('always run')
    print(i)

print('-----------------------')

s = 'hello'
for i in range(len(s)):
    print(i, s[i])

print('-----------------------')
#writing the previous code better
for i, c in enumerate(s):
    print(i, c)