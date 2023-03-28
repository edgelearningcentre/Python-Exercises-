"""
Title     : Python: Division
Language  : Python
Author    : edgelearningcentre
Created   : 28 March 2023
Problem   : https://www.hackerrank.com/challenges/python-division/problem
"""
if __name__ == "__main__":
  a = int(input())
  b = int(input())
  output = [lambda a, b: a//b,
            lambda a, b : a/b ]
  print(output[0](a,b))
  print(output[1](a,b))
