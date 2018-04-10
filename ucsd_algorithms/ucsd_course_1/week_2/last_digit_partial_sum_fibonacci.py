#python3

input=input()
inputs=[int(x) for x in input.split()]
a=inputs[0]
b=inputs[1]

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

def fib_iter_sum(start, n):
    #print('start {}'.format(start))
    #print('n {}'.format(n))
    sum=0
    a, b, c = [1, 1, 0]
    if n < 2: return n
    for i in range(n-1):
        if i >= start-1:  
            sum+=a
            #print('sum {}'.format(sum))
        c=(a+b) % 10
        #c=(a+b)
        a=b
        b=c

    #print('last a {}'.format(a))
    #print('sum {}'.format(a + sum))
    return (a + sum) % 10

pp=pisano_period(10)
#basically reduce the large number to its cyclic period
x=b%pp #n
y=a%pp #start
print(fib_iter_sum(y, x))
