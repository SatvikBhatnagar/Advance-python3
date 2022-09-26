# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 11:29:50 2022

@author: satvik
"""

s = [1, 2, 3]
len(s)

from math import sqrt
sqrt(4)

import math
math.pi
math.exp(1)

def func_1():
    print('running func_1')
func_1()

def func_2(a:int, b:int): #this is only for documentation
    return a * b
func_2('a', 3)
func_2(2,3)
func_2(2, [2,3,4])

def func_3():
    return func_4()

def func_4():
    return 'running func_4'

func_3() #this will work because python doesn't look inside a function until it is called upon

type(func_3)

my_func = func_4
func_4()
my_func()