"""
Title     : Python If-Else
Language  : Python
Author    : edge learning centre
Created   : 28 March 2023
Problem   : https://www.hackerrank.com/challenges/py-if-else/problem
"""
n = int(input())
output = lambda n : 'weird' if n % 2 == 1 or n in range(5, 21) else 'Not weird'
print(output(n))
