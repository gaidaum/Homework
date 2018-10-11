#6 

n = int(input())

for i in range(0,n):

    string = input()
    
    for j in range(0,len(string)):
        if j %2 == 0:
            print(string[j], end='')
            
    print(" ", end= '')
    
    for j in range(0, len(string)):
        if j % 2 != 0:
            print(string[j], end= '')
            
    print("")

#6 shorter way 
n = int(input())

for i in range(0,n):
    string = input()
    
    even, odd = string[::2], string[1::2]
    print(even + " " + odd)


#7 
#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input().strip())
arr = [int(l) for l in input().strip().split(' ')]
nums = map(str, arr [::-1])
print(" ".join(nums))    



#9 recursion factorial *******************



# Complete the factorial function below.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n *factorial (n-1)



#*******decimal to binary function*********

findBinary(decimal)
   if (decimal == 0)
      binary = 0
   else
      binary = decimal % 2 + 10 * (findBinary(decimal / 2)



# full decimal to binary function with inputs


def binary(x):
	
	if x > 1:
		binary(x//2)
	print(x%2, end= '')

num = int(input('Enter a number: '))
print ('Your binary number is : ')
binary(num)


# how the decimal to binary works >>>
# 45 % 2 = 1 -> 45 // 2 = 22 
# 22 % 2 = 0 -> 22 // 2 = 11
# 11 % 2 = 1 -> 11 // 2 = 5 
# 5 % 2 = 1 -> 5 // 2 = 2 
# 2 % 2 = 0 -> 2 // 2 = 1 
# 1 % 2 = 1 