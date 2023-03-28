"""
Title     : Print Function
Language  : Python
Author    : edgelearningcentre
Created   : 28 Mar , 2023
Problem   : https://www.hackerrank.com/challenges/python-print/problem
"""

if __name__ == "__main__":
    n = int(input())
    print("".join([str(i) for i in range(1,n+1)]))
