#python3

def fib_iter(n):
    if n < 2: return n
    a, b, c = [1, 1, 0] 
    for i in range(n - 1):
        c = (a + b) % 10 # make this modulo 10, instead of return a % 10 due to runtime issues, this will give you the proper last digit, but not the correct actual number
        a = b
        b = c
    
    return a


n = int(input())

#print('should be 6 if input is 999999 {}'.format(fib_iter(n)))
print(fib_iter(n))

