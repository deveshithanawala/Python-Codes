# -*- coding: utf-8 -*-
"""Task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/111iR-aHHSDbZXLMXHgciRbviJ4pWP97a

HackerRank Task 2 Python:


Given an integer, n , perform the following conditional actions:





*   If n is odd, print Weird
*   If n is even and in the inclusive range of  to , print Not Weird

*   If n is even and in the inclusive range of  to , print Weird
*   If n is even and greater than , print Not Weird
"""

n=int(input())
if (n%2==1):
    print('Weird')
elif(2<=n<=5 and n%2==0):
    print('Not Weird')
elif(6<=n<=20 and n%2==0):
    print('Weird')
elif(n%2==0 and n>20):
    print('Not Weird')

