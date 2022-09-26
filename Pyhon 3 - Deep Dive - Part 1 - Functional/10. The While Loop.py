# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 19:52:45 2022

@author: satvik
"""

# while loop
i = 0
while i < 5:
    print(i)
    i += 1

j = 50
while True:
    print(j)
    if j >= 50:
        print('something before break')
        break
        print('something after break')

# ------------------------------------------

'''
min_length = 2
name = input("Please enter your name: ")

while not(len(name) >= min_length and name.isprintable() and name.isalpha()):
    name = input("Please enter your name: ")
print("Hello, {0}".format(name))
'''

min_length = 2

while True:
    name = input("Please enter your name: ")
    if (len(name) >= min_length and name.isprintable() and name.isalpha()):
        break

print("Hello, {0}".format(name))

# ------------------------------------------

a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)

l = [1, 2, 3]
val = 10

found = False
idx = 0
while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1

if not found:
    l.append(val)
print(l)

# ------------------------------------------
l = [1, 2, 3]
val = 10
idx = 0
while idx < len(l):
    if l[idx] == val:
        break
    idx += 1
else:  # this will only run if the while loop ran without encountering the break statement
    l.append(val)
print(l)

# ------------------------------------------------------------------------------

# try...except...finally
a = 10
b = 0
try:
    a/b
except ZeroDivisionError:
    print('division by 0')
finally:
    print('this always executes')

a = 0
b = 2

while a < 4:
    print('-----------')
    a += 1
    b -= 1

    try:
        a / b
    except ZeroDivisionError:
        print("{0}, {1} - division by 0".format(a, b))
        continue
    finally:
        print("{0}, {1} - always executes".format(a, b))

    print("{0}, {1} - main loop".format(a, b))
# --------------------------
