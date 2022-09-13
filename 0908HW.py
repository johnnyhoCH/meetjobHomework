# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 22:26:10 2022

@author: user
"""

#0,1,1,2,3,5,8,13,21,34......

n = eval(input())
fib = []
fib1 = []
total = 0

for i in range(n):
    if i == 0:
        a = 0
    elif i == 1:
        a = 1
        fib = [0,1]
        fib1 = [0,1]
    else:
        a = fib[0]+fib[1]
        del(fib[0])
        fib.append(a)
        fib1.append(a)
    total += a
print(fib1)
    
print(total)
    
        
        
    


