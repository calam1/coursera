import collections

Stuff = collections.namedtuple('Stuff', 'value weight')
stuff_list = []
stuff_list.append(Stuff(value=60, weight=10))
stuff_list.append(Stuff(value=100, weight=20))
stuff_list.append(Stuff(value=120, weight=30))

def knapsack_bounded_recursive(stuffs, m, capacity):
    if capacity <= 0: return 0
    if m <= 0: return 0

    if stuffs[m-1].weight <= capacity:
        return max(knapsack_bounded_recursive(stuffs, m-1, capacity), stuffs[m-1].value + knapsack_bounded_recursive(stuffs, m-1, capacity - stuffs[m-1].weight))
    else:
        return knapsack_bounded_recursive(stuffs, m-1, capacity)

print('recursive bounded knapsack answer should be 220 {}'.format(knapsack_bounded_recursive(stuff_list, len(stuff_list), 50)))

def knapsack_bounded_dp(stuffs, capacity):
    solution = [[0 for _ in range(len(stuffs)+1)] for j in range(capacity+1)]

    for i in range(capacity+1):
        for j in range(len(stuffs)+1):
            if i == 0 or j == 0:
                solution[i][j] = 0
            else:
                if stuffs[j-1].weight <= i:
                    solution[i][j] = max(solution[i][j-1],
                                         stuffs[j-1].value + solution[i - stuffs[j-1].weight][j-1])
                else:
                    solution[i][j] = solution[i][j-1]

    #print(solution)
    return solution[capacity][len(stuffs)]

print('dp bounded knapsack answer should be 220 {}'.format(knapsack_bounded_dp(stuff_list, 50)))


stuff_list_ub = []
stuff_list_ub.append(Stuff(value=10, weight=1))
stuff_list_ub.append(Stuff(value=40, weight=3))
stuff_list_ub.append(Stuff(value=50, weight=4))
stuff_list_ub.append(Stuff(value=70, weight=5))


def knapsack_unbounded_recursive(stuffs, capacity, answers):
    max_value = 0

    for i in range(len(stuffs)):
        if stuffs[i].weight <= capacity:
            max_value = max(max_value, stuffs[i].value + knapsack_unbounded_recursive(stuffs, capacity - stuffs[i].weight, answers))
        answers[capacity] = max_value

    #print(answers)
    return answers[capacity]

cap = 8
ans = [0 for _ in range(8+ 1)]
print('recursive unbounded knapsack answer should be 110 {}'.format(knapsack_unbounded_recursive(stuff_list_ub, cap, ans)))

# MY PREFERRED RECURSIVE SOLUTION
def knapsack_unbounded_recursive_2(stuffs, capacity):
    max_value = 0

    for i in range(len(stuffs)):
        if stuffs[i].weight <= capacity:
            max_value = max(max_value, stuffs[i].value + knapsack_unbounded_recursive_2(stuffs, capacity - stuffs[i].weight))

    return max_value

print('recursive 2 unbounded knapsack answer should be 110 {}'.format(knapsack_unbounded_recursive_2(stuff_list_ub, 8)))


def knapsack_unbounded_dp(stuffs, capacity):
    max_values = [0 for _ in range(capacity + 1)]

    for i in range(capacity + 1):
        for j in range(len(stuffs)):
            if stuffs[j].weight <= i:
                max_values[i] = max(max_values[i], max_values[i - stuffs[j].weight] + stuffs[j].value)

    #print(max_values)
    return max_values[capacity]

print('dp unbounded knapsack answer should be 110 {}'.format(knapsack_unbounded_dp(stuff_list_ub, 8)))
