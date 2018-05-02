# Uses python3
import sys

# isn't always correct, looks like greedy approach
def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

#you can mult by 2, mult by 3, or add 1
# algo is slightly different in this link, but explains how to get the list of numbers http://thisthread.blogspot.com/2018/02/primitive-calculator.html
def dp_sequence(n):
    sequence = []  # final solution

    # buffer
    buffer = [0] * (n + 1)

    # reverse all the actions, to move towards 1, thus subtract 1, div by 2 and div by 3
    # like finding min change for coins
    for i in range(1, len(buffer)):
        buffer[i] = buffer[i - 1] + 1

        if (i % 2 == 0):
            buffer[i] = min(1 + buffer[i // 2], buffer[i])

        if (i % 3 == 0):
            buffer[i] = min(1 + buffer[i // 3], buffer[i])

    print('buffer values {}'.format(buffer))

    while (n > 1):
        sequence.append(n)

        # If the previous element in the cache is the current value of the cache minus one, I got there adding one,
        # so I here apply the inverse operator, decreasing target by one
        if (buffer[n - 1] == buffer[n] - 1):
            n = n - 1
        # If the current target is divisible by 2, and the cache at position current divided by two is actually the
        # value of the current element of the cache minus one, we got there multiplying by two. So I apply the inverse to backtrace.
        elif (n % 2 == 0 and (buffer[n // 2] == buffer[n] - 1)):
            n = n // 2
        # explanation similar to divide by 2
        elif (n % 3 == 0 and (buffer[n // 3] == buffer[n] - 1)):
            n = n // 3

    sequence.append(1)
    return reversed(sequence)

# count only
def recursive_sequence(n):
    x, y, z = n, n, n

    if n <= 1:
        return 0

    if n % 2 == 0:
        #print(n)
        x = recursive_sequence(n // 2)

    if n % 3 == 0:
        #print(n)
        y = recursive_sequence(n // 3)

    z = recursive_sequence(n-1)

    return 1 + min(x, y, z)


input = sys.stdin.read()
n = int(input)
# sequence = list(optimal_sequence(n))
s = recursive_sequence(n)
print('recursive {}'.format(s))
sequence = list(dp_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
