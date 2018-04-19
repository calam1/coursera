#Uses python3

import sys
from functools import cmp_to_key

def cmp(x, y):
    return -1 if x<y else ( 0 if x==y else 1)

def largest_number(x):
    return ''.join(sorted((str(n) for n in x),
        key=cmp_to_key(lambda x,y:cmp(y+x, x+y))))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
