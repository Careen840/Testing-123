# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 00:59:53 2020

"""
##Fizzbuzz question


for i in range(1, 100):
    if (i% 3==0) and (i% 5==0):
        print("FizzBuzz")
    elif i % 3== 0:
        print("Fizz")
    elif i % 5==0 :
        print("Buzz")
    else:
        print(i)
        
        
###second solution
        
def input(i):
    if (i% 3==0) and (i% 5==0):
        return "FizzBuzz"
    elif i % 3== 0:
        return"Fizz"
    elif i % 5==0 :
        return"Buzz"
    return i
print (input(27))

        