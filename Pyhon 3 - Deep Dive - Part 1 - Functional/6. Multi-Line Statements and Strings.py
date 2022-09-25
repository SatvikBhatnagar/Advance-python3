# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 04:25:03 2022

@author: satvik
"""

#Physical line of code -- end with a physical newline character
#logical likne of code -- end with a logical NEWLINE token

#implicit and explicit conversion

'''Implicit
    -expressions in:
        list literals: []
        tuple literals: ()
        dictionary literals: {}
        sets: {}
        function arguments / parameters
    -supports inline comments'''

'''Explicit
    -You can break up statements over multiple lines explicitly,
    by using the \ (backslash) character

    -Multli-line statements are not implicity converted to a
    single logical line.

    -Comments cannot be part of a statement, not even a multi-line
    statement'''

#Multi-Line String Literals - non-visible characters (newlines, tabs, etc.) are actually part of the string
'''This is
a multi-line string'''
"""This is
a multi-line string"""

'''Comments are not part of your code
    but docstrings are'''

a = [1, 2, 3]

b = [1, 2,
     3, 4, 5]

c = [1 #item1
     , 2 #item 2
     , 3 #item 3
     ]

d = (1,
     2, #comment
     3 #comment
     )

e = {'key1': 1, #value for key 1
     'key2': 2 #value for key 2
     }

def my_func(a, #this is used to indicate...
            b, #comment
            c):
    print(a, b, c)


my_func(10, #comment
        20, #comment
        30 #comment
        )

g = 10
h = 20
i = 30

if g > 5 and h > 10 and i > 20:
    print('yes')

if g > 5 \
    and h > 10 \
    and i > 20:
    print('yes')

j = '''this is a string'''
print(j)

k = '''
this is
a string '''
print(k)

l = 'this\nis also string'
print(l)

m = '''this
    is a string
        that is created over multiple lines'''
print(m)

def My_func():
    a = '''a multi-line string
    that is indented in the second line'''
    return a
print(My_func())