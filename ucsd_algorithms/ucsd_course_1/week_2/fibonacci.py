#python3

def fib_recursive(n):
    if n < 2: return n
    return  fib_recursive(n-2) + fib_recursive(n-1)

def fib_iter(n):
    if n < 2: return n
    a, b, c = [1, 1, 0] 
    for i in range(n - 1):
        c = a + b
        a = b
        b = c

    #print('a {} b {} c {}'.format(a, b, c))
    return a

def fib_dynamic(n):
    solution = [0] * (n+1)

    for i in range(n+1):
        # first 2 lines seed the data
        if i == 0: solution[i] = 0
        elif i == 1 or i == 2: solution[i] = 1
        else: solution[i] = solution[i-2] + solution[i-1]

    #print (solution)
    return solution[n]


n = int(input())

# 1 1 2 3 5 8 13 21
#print('fib_recursive {}'.format(fib_recursive(n)))
#print('fib_iter {}'.format(fib_iter(n)))
#print('fib_dynamic {}'.format(fib_dynamic(n)))
print(fib_dynamic(n))


