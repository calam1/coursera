def selection_sort(values):
    for i in range(len(values)):
        min_position = i
        for j in range(i+1, len(values)):
            # find the smallest value
            if values[min_position] > values[j]:
                min_position = j
        # after finding the smallest value, swap
        values[min_position], values[i] = values[i], values[min_position]



values = [3, 1, 2, 8 ,3]

selection_sort(values)
#n^2
print('after sort {}'.format(values))
