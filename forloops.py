"""
Title     : Loops
Language  : Python
Author    : edgelearningcentre
Created   : 25 March, 2023
Problem   : https://www.hackerrank.com/challenges/python-loops/problem
"""
if __name__ == "__main__":
  i = 0
  n = int(input())
  for i in range (n):
    if i < n:
      print (i * i)
      i += 1
