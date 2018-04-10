#python3

def fib_iter(n, m):
    if n < 2: return n
    a, b, c = [1, 1, 0] 
    for i in range(n - 1):
        c = (a + b) % m
        a = b
        b = c
    
    return a

# general approach in PDF
# if F(2015) - 2015 fib sequence and mod is 3
## the pisano periond = 8 - need to figure out how to calcualte pisano period
## take 2015 / 8 = 251 , take 2015 % 8 = 7
## the mod remainder becomes the sequence F(7) mod 3 = 1
## F(7) happens to be 13 and 13 % 3 = 1

#pisano period
def pisano_period(m):
    previous = 1
    current = 1
    result = 1

    while not(previous == 0 and current == 1):
        buffer = (previous + current) % m
        previous = current
        current = buffer

        result += 1

    return result

def large_fib(n, m):
    '''large_fib'''
    pp = pisano_period(m) #pisano periond
    #print('pp {}'.format(pp))
    pisano_mod_result = n % pp
    #print('pisano_mode_result {}'.format(pisano_mod_result))
    result = fib_iter(pisano_mod_result, m)
    #print(result)
    return result

input = input()
inputs = [int(i) for i in input.split()]
n = inputs[0]
m = inputs[1]

#print(pisano_period(m))
print(large_fib(n, m))



