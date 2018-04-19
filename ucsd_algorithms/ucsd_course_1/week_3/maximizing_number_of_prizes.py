#python3
import sys

# don't quite understand this problem  help at https://repl.it/@ahmedtadde/Maximizing-the-Number-of-Prize-Places-in-a-Competition
def optimal_summands(value):
    k = 1
    sums = []
    while True:
        if value <= 2*k:
            sums.append(value)
            break
        else:
            sums.append(k)
            value = value - k
            k += 1
    return sums 

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

