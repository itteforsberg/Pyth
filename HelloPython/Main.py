#!/usr/bin/env python3
import xyz
import doctest
import unittest
import sys
from math import *

fett = 23
print(fett)

sum = lambda x, y : x + y
print(sum(3, 4))

def fahrenheit(T):
    return ((float(9)/5)*T + 32)

temperatures = (36.5, 37, 37.5, 38, 39)
F = map(fahrenheit, temperatures)
print (list(F))

temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))
print(temperatures_in_Fahrenheit)

F = list(map(lambda x: (float(9)/5)*x + 32, temperatures))
print(F)

a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
fett = list(map(lambda x,y:x+y, a,b))

print(fett)

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)
