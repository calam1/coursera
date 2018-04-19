#python3
import math
from itertools import count

#input = input()
#inputs = [int(i) for i in input.split()]
#a = inputs[0]
#b = inputs[1]

def primeFactors(n):
    solution = []
    while n % 2 == 0:
        #print(2)
        solution.append(2)
        n = n // 2

    # the while loop above gets us to a point where n must be odd
    # thus you can skip 2, i.e. every other
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            #print(i)
            solution.append(i)
            n = n // i

    if n > 2:
        #print(n)
        solution.append(n)

    return solution

def prime_factors(n):
    factors = []
    #for i in count(2):
    for i in range(2, n+1):
        while n % i == 0:
            factors.append(i)
            n //= i
            #print('while factors {}'.format(factors))
        # gets the last numver
        if 2 * i > n:
            #print('i {}'.format(i))
            #print('n {}'.format(n))
            factors.append(n)
            return factors


print('primeFactors {}'.format(primeFactors(180)))
print('prime_factors {}'.format(prime_factors(180)))
