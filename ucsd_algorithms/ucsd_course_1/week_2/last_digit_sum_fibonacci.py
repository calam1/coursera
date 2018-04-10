#python3

n=int(input())

# runs slow on large numbers
def fib_iter_sum_slow(n):
    sum=0
    a, b, c = [1, 1, 0]
    if n < 2: return n
    for i in range(n-1):
        #print('a {}'.format(a))
        sum+=a
        c=(a+b) % 10
        a=b
        b=c

    return (a + sum) % 10

# very similar to fib_iterative
def pisano_period(m):
    #a, b, c
    prev, cur, buffer = [1, 1, 0]
    result = 1
    #while not a, b
    while not(prev==0 and cur==1):
        #c=a+b
        buffer=(prev+cur) % m
        #a=b
        prev=cur
        #b=c
        cur=buffer
        #add 1
        result+=1

    return result

def fib_iter_sum(n):
    sum=0
    a, b, c = [1, 1, 0]
    if n < 2: return n
    for i in range(n-1):
        #print('a {}'.format(a))
        sum+=a
        c=(a+b) % 10
        a=b
        b=c

    #print('last a {}'.format(a))
    return (a + sum) % 10

pp=pisano_period(10)
x=n%pp
print(fib_iter_sum(x))
