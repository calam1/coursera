#python3

def change(amount, coins):
    running_total = 0
    count = 0
    for i in range(len(coins)):
        while running_total + coins[i] <= amount:
            count += 1
            running_total += coins[i]
    return count

coins = [1, 5, 10]
coins.sort(reverse=True)

#print(coins)
a = int(input())

print(change(a, coins))
