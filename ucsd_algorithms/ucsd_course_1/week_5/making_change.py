#python3
import sys

def get_change(amount):
    coins = [1, 3, 4]
    solution = [0 for i in range(amount+1)]

    for i in range(amount+1):
        min_coins = float('inf')
        for j in coins:
            if i == 0:
                solution[i] = 0
            else:
                if j <= i:
                    min_coins = min(min_coins, 1 + solution[i - j])
                solution[i] = min_coins
    
    return solution[amount]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

