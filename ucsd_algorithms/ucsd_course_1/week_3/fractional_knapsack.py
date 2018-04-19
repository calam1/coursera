# Uses python3
import sys

# too much time for large datasets
def orig_get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    stuff = []
    # break down the stuff  to 1 unit and figure out the value ratio and then sort
    for i in range(len(weights)):
        r = values[i] / weights[i]
        for j in range(weights[i]):
            stuff.append(r)
    stuff.sort(reverse=True)
    #print('stuff {}'.format(stuff))

    i = 0
    while i < len(stuff):
        if capacity > 0:
            value += stuff[i]
            #print('value {} stuff[{}] = {}'.format(value, i, stuff[i]))
            capacity -= 1 # all units are 1
            #print('capacity {}'.format(capacity))
            i += 1
        elif capacity == 0:
            break
        else:
            i += 1

    return value


def get_optimal_value(capacity, weights, values):
    value = 0.

    stuff = []
    for i in range(len(values)):
        r = values[i] / weights[i]
        stuff.append((r, weights[i])) # append tuple to list

    stuff.sort(reverse=True)
    #print(stuff)

    for i in range(len(stuff)): # iterate through the ratios and how many times they occur
        if capacity != 0:
            for j in range(stuff[i][1]):
                if capacity > 0:
                    value += stuff[i][0]
                    capacity -= 1
                else:
                    break
        else:
            break

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
