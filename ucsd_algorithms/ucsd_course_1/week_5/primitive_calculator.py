# Uses python3
import sys

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

def dp_sequence(n):
    buffer = [0 for i in range(n+1)]
    buffer[1] = 1 # starting number

    for i in range(1, n+1):
        if not buffer[i]: continue
        if buffer[i+1] == 0 or buffer[i+1] > buffer[i] + 1:
            buffer[i+1] = buffer[i] + 1

    solution = []
    while n > 1:
        solution.append(n)
        if buffer[n-1] == buffer[n] - 1:
            n = n-1
        if n%2 == 0 and buffer[n//2] == buffer[n] - 1:
            n = n//2
        solution.append(1)
        return reversed(solution)



#input = sys.stdin.read()
#n = int(input)
#sequence = list(optimal_sequence(n))
#print(len(sequence) - 1)
#for x in sequence:
#    print(x, end=' ')


#seq = optimal_sequence(5)
seq = dp_sequence(5)
for i in seq: print(i, end=' ')
