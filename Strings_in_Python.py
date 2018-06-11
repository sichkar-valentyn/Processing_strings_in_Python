# File: Strings_in_Python.py
# Description: Methods for processing strings in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Methods for processing strings in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Processing_strings_in_Python (date of access: XX.XX.XXXX)

# Standard methods for processing strings


# Using 'in' for strings
print('abc' in 'abcba')
print('abce' in 'abcba')


# Method 'find' returns position from which the string begins
print('cabcd'.find('abc'))  # Position is 1
print('cabcd'.find('abe'))  # Position is -1 because there is no such string
# Showing the documentation of method 'find'
print(str.find.__doc__)
# Starting to find from specific position
print('cabcd'.find('abc', 1))  # Result is 1
# Searching in sliced string
print('cabcd'[1:].find('abc'))  # Result is 0


# Method 'index' is quite the same as 'find' but through exception if there is no such string
print('cabcd'.index('abc'))  # Position is 1
# print('cabcd'.index('abe'))  # Through exception ValueError


# Method 'startswith' shows if the string begins from substring
s = 'The man in black fled across the desert, and others followed'
print(s.startswith('The man in black'))  # Result is True
# Showing the documentation for method 'startswith'
print(s.startswith.__doc__)
# We can use tuple as prefix
print(s.startswith(('The woman', 'The dog', 'The man in black')))


# Method 'endswith' shows if th e string ends with substring
s = 'image.png'
print(s.endswith('.png'))


# Method 'count' shows how many times substring is included in string
s = 'abacaba'
print(s.count('aba'))  # Result is 2
# Showing the documentation for method 'count'
print(s.count.__doc__)
# It shows non-overlapping occurrences
s = 'ababa'
print(s.count('aba'))  # Result is 1


# Left and right searching for substring in the string
s = 'abacaba'
print(s.find('aba'))  # Result is 0
print(s.rfind('aba'))  # Result is 4


# Method to make all letters in the string in lower or upper cases
s = 'The man in black fled across the desert, and others followed'
print(s.lower())
print(s.upper())
print(s.count('the'))  # Result is 2
print(s.lower().count('the'))  # Result is 3


# Method to replace some elements to another
s = '1,2,3,4,5'
print(s)
print(s.replace(',', ', '))
# Showing the documentation for method 'replace'
print(s.replace.__doc__)
# Replacing only limited number of elements
print(s.replace(',', ', ', 2))


# Method to divide string into substring by specific element
s = '1 2 3 4 5'
print(s.split(' '))  # Result is a list ['1', '2', '3', '4', '5']
# Showing the documentation for method 'split'
print(s.split.__doc__)
# Splitting only limited number of elements
print(s.split(' ', 2))  # Result is a list ['1', '2', '3 4 5']
# If don't specify any prefixes, the method will delete all gaps and split by gap
s = '1 \t\t   2    3   4        5         '
print(s.split())  # Result is a list ['1', '2', '3', '4', '5']
# Also, there is left strip and right strip
s = '     1, 2, 3, 4, 5      '
print(repr(s.rstrip()))  # Result is '     1, 2, 3, 4, 5'
print(repr(s.lstrip()))  # Result is '1, 2, 3, 4, 5      '
print(repr(s.strip()))  # Result is '1, 2, 3, 4, 5'


# Method to join elements from sum sequence with specific element
n = map(str, [1, 2, 3, 4, 5])
print(repr(' '.join(n)))  # Result is '1 2 3 4 5'


# Method for formatting strings
capital = 'London is the capital of Great Britain'
template = '{} is the capital of {}'
print(template.format('London', 'Great Britain'))
print(template.format('Vaduz', 'Liechtenstein'))
# Showing the documentation for the method 'format'
print(template.format.__doc__)
# It's possible to right the number of elements and change there order
template = '{1} is the capital of {0}'
print(template.format('London', 'Great Britain'))
# Also, it is possible to use named arguments
template = '{capital} is the capital of {country}'
print(template.format(capital='London', country='Great Britain'))
# Another example to show responses from requests
import requests
template = 'Response from {0.url} with code {0.status_code}'
res = requests.get('http://docs.python.org/3.5/')
print(template.format(res))
# Using 'format' to round the float numbers
from random import random
x = random()
print(x)
print('{:.3}'.format(x))

