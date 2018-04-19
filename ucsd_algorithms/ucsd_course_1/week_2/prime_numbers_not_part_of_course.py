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

#The first for loop ranges till the upper limit entered by the user.
#The count variable is first initialized to 0.
#The inner for loop ranges from 2 to the half of the number so 1 and the number itself aren’t counted as divisors.
#The if statement then checks for the divisors of the number if the remainder is equal to 0.
#The count variable counts the number of divisors and if the count is lesser or equal to 0, the number is a prime number.
#If the count is greater than 0, the number isn’t prime.
#The final result is printed.
def prime_numbers(n):
    solution = []
    for i in range(2, n+1):
        k = 0
        for j in range(2, int(i//2) + 1):
            if (i%j == 0):
                k+=1
        if k<= 0: solution.append(i)

    return solution

print('prime_numbers {}'.format(prime_numbers(45)))
