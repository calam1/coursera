#python3

import sys

input = input()
inputs = [int(i) for i in input.split()]
a = inputs[0]
b = inputs[1]
#print('a {} b {}'.format(a, b))

def naive_gcd(a, b):
    maximum = -sys.maxsize-1
    for i in range(1, a+b+1):
        if a % i == 0 and b% i == 0:
            maximum=i

    return maximum

def euclidean_solution(A, B):
  # base case
  if B == 0: return A

  remainder = A % B
  #print('remainder {}'.format(remainder))
  return euclidean_solution(B, remainder)

#print('naive solution {}'.format(naive_gcd(a, b)))
#print('euclidean solution {}'.format(euclidean_solution(a, b)))
print(euclidean_solution(a, b))
