# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 23:30:40 2022

@author: satvik
"""

#identifiers names are case sensitive

#conventions
"""
    _my_var -- single underscore -- convention that it is for 'internal use' or 'private' objects
                                 -- objects named this way will not get imported by a statement such as:
                                        from module import *
    __my_var -- double underscore -- used to 'mangle' class attributes - useful in ingeritance chains

    __my_var__ -- used for system-defined names that have special meaning to the interpreter.
               -- don't invent them, stick to the ones pre-defined by Python!

"""
#other naming conventions
"""
    Paackages -- short, all-lowercase names. Preferably no underscores. eg. utilities
    Modules -- short, all-lowercase names. Can have underscores. eg. db_utils, dbutils
    Classes -- CapWords (upper camel case) convention. eg. BankAccount
    Functions -- lowercase, words separated by underscores (snake_case). eg. open_account
    Variables -- lowercase, words separated by underscores (snake_case). eg. account_id
    Constants -- all-uppercase, words separated by underscores. eg. MIN_APR
"""
#PEP 8 Style Guide - https://peps.python.org/pep-0008/