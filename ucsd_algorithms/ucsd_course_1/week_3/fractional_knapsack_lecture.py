import collections

Stuff = collections.namedtuple('Stuff', 'name value weight')
X = Stuff(name='x', value=20, weight=4)
Y = Stuff(name='y', value=18, weight=3)
Z = Stuff(name='z', value=14, weight=2)

Unit = collections.namedtuple('Unit', 'name value count weight')

def breakdown_stuff_per_unit(stuff):
    value = stuff.value
    weight = stuff.weight
    unit_value = value // weight
    unit = Unit(stuff.name, value=unit_value, count=weight, weight=1)
    return unit

x_unit = breakdown_stuff_per_unit(X)
y_unit = breakdown_stuff_per_unit(Y)
z_unit = breakdown_stuff_per_unit(Z)

units = [x_unit, y_unit, z_unit]

def sort_by_value(list, attribute, reverse=False):
    list.sort(key=lambda x: getattr(x, attribute), reverse=reverse)

sort_by_value(units, 'value', True)

sorted_list = []

for i in range(len(units)):
    #print(units[i])
    for j in range(units[i].count):
        #print(units[i].value)
        sorted_list.append(units[i])

#print(sorted_list)

def optimize_fractional_knapsack(items, capacity):
    stuff = []
    i = 0
    while i < len(items):
        if items[i].weight <= capacity:
            stuff.append(items[i].value)
            capacity -= items[i].weight
            while i+1 < len(items) and items[i+1].weight <= capacity:
                stuff.append(items[i+1].value)
                capacity -= items[i+1].weight
                i += 1
        else:
            i += 1

    return stuff

# answer should be 42
print(optimize_fractional_knapsack(sorted_list, 7))
