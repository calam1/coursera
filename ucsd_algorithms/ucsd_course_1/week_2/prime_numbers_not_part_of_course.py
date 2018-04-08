#python3

import math

#input = input()
#inputs = [int(i) for i in input.split()]
#a = inputs[0]
#b = inputs[1]

# Sieve of Erastothenes to generate a list of primes up to a number
# https://inventwithpython.com/hacking/chapter23.html
def primeSieve(size):
    # returns a list of prime numbers
    sieve = [True] * size # generate an array of True
    sieve[0] = False # 0 is not prime
    sieve[1] = False # 1 is not prime
    for i in range(2, int(math.sqrt(size)) + 1):
        pointer = i * 2
        while pointer < size:
            sieve[pointer] = False
            pointer += i

    primes = []
    for i in range(size):
        if sieve[i] == True:
            primes.append(i)

    return primes

print('primes of 30 {}'.format(primeSieve(30)))
print('primes of 45 {}'.format(primeSieve(45)))
