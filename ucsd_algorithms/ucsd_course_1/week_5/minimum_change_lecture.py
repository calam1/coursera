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


#print('not always correct {}'.format(minNumberOfCoins(32, [1, 8, 20])))

def findMinCoins(coins, amount):
    minCoins = amount  # max out the count initially
    if len(coins) == 0 or amount == 0:
        return 0
    elif amount in coins:
        return 1
    elif amount < min(coins):  # if amount is smaller than smallest coin
        return float("inf")
    else:
        for i in coins:
            if i <= amount:
                numCoins = 1 + findMinCoins(coins, amount - i)
                minCoins = min(minCoins, numCoins)

    return minCoins


print('recursive {}'.format(findMinCoins([1, 8, 20], 32)))


def finMinCoinsDynamicProgramming(coins, amount):
    solution = [0 for i in range(amount + 1)]  # find amount for every cent of amount

    for i in range(amount + 1):
        smallest = float("inf")
        for j in range(len(coins)):
            if (i == 0):
                solution[i] = 0
            else:
                if coins[j] <= i:
                    smallest = min(smallest, solution[i - coins[j]])
                solution[i] = 1 + smallest

    print(solution)
    return solution[amount]


def findAllCountsChange(coins, amount):
    solution = [[0 for i in range(amount+1)] for j in range(len(coins) + 1)]

    for i in range(len(coins) + 1):
        for j in range(amount + 1):
            if i == 0:
                solution[i][j] = 0
            elif j == 0:
                solution[i][j] = 1
            else:
                if coins[i - 1] <= j: # -1 due to indexing
                    solution[i][j] = solution[i][j - coins[i-1]] + solution[i-1][j]
                else:
                    solution[i][j] = solution[i-1][j]

    return solution[len(coins)][amount]


print('dynamic if use greedy will give wrong answer {}'.format(finMinCoinsDynamicProgramming([1, 8, 20], 32)))
#print('dynamic find all counts {}'.format(findAllCountsChange([1, 2, 3], 5)))
print('dynamic find all counts {}'.format(findAllCountsChange([1, 8, 20], 32)))


def findAllCountChangeDPDiffAxis(coins, amount):
    # solution[amount][coins] 5(+1)- coins   3(+1) - len(coins)
    # c c c c
    # c c c c
    # c c c c
    # c c c c
    # c c c c
    # c c c c
    # c c c c
    solution = [[0 for i in range(len(coins)+1)] for j in range(amount+1)]
    #print(solution)

    for i in range(amount+1):
        for j in range(len(coins)+1):
            if i == 0:
                solution[i][j] = 1
            elif j == 0:
                solution[i][j] = 0
            else:
                if coins[j-1] <= i:
                    solution[i][j] = solution[i - coins[j-1]][j] + solution[i][j-1]
                else:
                    solution[i][j] = solution[i][j-1]
    print(solution)
    return solution[amount][len(coins)]

#print('dynamic diff axis {}'.format(findAllCountChangeDPDiffAxis([1, 2, 3], 5)))
print('dynamic diff axis {}'.format(findAllCountChangeDPDiffAxis([1, 8, 20], 32)))

def findAllCountChange_rec(coins, coins_length, amount):
    if amount == 0: return 1
    if amount < 0: return 0
    if coins_length == len(coins): return 0

    return findAllCountChange_rec(coins, coins_length+1, amount) + findAllCountChange_rec(coins, coins_length, amount - coins[coins_length])


print('find all change recursive {}'.format(findAllCountChange_rec([1, 2, 3], 0, 5)))

