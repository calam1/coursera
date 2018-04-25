
def allchange(coins, amount):
    solution = [[0 for i in range(len(coins)+1)] for j in range(amount+1)]

    for i in range(amount+1):
        for j in range(len(coins)+1):
            if i == 0:
                solution[i][j] = 1
            elif j == 0:
                solution[i][j] = 0
            else:
                if coins[j-1] <= i:
                    solution[i][j] = solution[i][j-1] + solution[i - coins[j-1]][j]
                else:
                    solution[i][j] = solution[i][j-1]

    return solution[amount][len(coins)]


def allchange_rec(coins, coins_length, amount):
    if amount == 0: return 1
    if amount < 0: return 0
    if coins_length == len(coins): return 0

    return allchange_rec(coins, coins_length+1, amount) + allchange_rec(coins, coins_length, amount - coins[coins_length])



coins = [1, 2, 3]
amt = 5
print(allchange(coins, amt))
print(allchange_rec(coins,0, amt))
