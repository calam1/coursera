# this does not always work makes assumptions of largest coins first, which apparently  is not
# always correct - Greedy approach
def minNumberOfCoins(amount, coins):
    if amount <= 0:
        return 0
    if amount in coins:
        return 1
    # this sort makes an assumption that is not always true
    for coin in sorted(coins, reverse=True):
        if coin <= amount:
            return 1 + minNumberOfCoins(amount - coin, coins)

print('not always correct {}'.format(minNumberOfCoins(32, [1, 8, 20])))


import math

def findMinCoins(coins, amount):
    minCoins = amount # max out the count initially
    if len(coins)== 0 or amount==0:
        return 0
    elif amount in coins:
        return 1
    elif amount < min(coins): # if amount is smaller than smallest coin
        return float("inf")
    else:
        for i in coins:
            if i <= amount:
                numCoins = 1 + findMinCoins(coins, amount - i)
                minCoins = min(minCoins, numCoins)

    return minCoins

print('recursive {}'.format(findMinCoins([1, 8, 20], 32)))


def finMinCoinsDynamicProgramming(coins, amount):
    solution = [0 for i in range(amount + 1)] # find amount for every cent of amount

    for i in range(amount + 1):
        smallest = float("inf")
        for j in range(len(coins)):
            if (i == 0):
                solution[i] = 0
            else:
                if coins[j] <= i:
                    smallest = min(smallest, solution[i - coins[j]])
                solution[i] = 1 + smallest

    #print(solution)
    return solution[amount]

print('dynamic {}'.format(finMinCoinsDynamicProgramming([1, 8, 20], 32)))

