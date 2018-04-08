#python3
import math
from itertools import count

input = input()
inputs = [int(i) for i in input.split()]
a = inputs[0]
b = inputs[1]

def greatest_common_divisor_iterative(x, y):
    """alse euclidean"""
    while(y):
        x, y = y, x % y

    return x

#print(greatest_common_divisor_iterative(a, b))

def lowest_common_multiple(x, y):
    """basically multiply both numbers and divide by greatest common divisor"""
    lcm = (x*y)//greatest_common_divisor_iterative(x, y)
    return lcm

print(lowest_common_multiple(a, b))
