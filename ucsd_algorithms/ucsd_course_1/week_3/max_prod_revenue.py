#Uses python3

import sys
from functools import reduce

def max_dot_product(a, b):
    a.sort(reverse=True)
    b.sort(reverse=True)

    c = [a * b for a, b in zip(a, b)]
    print(c)
    return reduce((lambda x, y: x + y), c)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))


