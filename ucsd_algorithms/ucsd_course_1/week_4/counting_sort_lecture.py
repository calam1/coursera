def counting_sort(aList, k):
    counter = [0] * (k + 1)
    for i in aList:
        counter[i] += 1

    idx = 0
    for i in range(len(counter)):
        while 0 < counter[i]:
            aList[idx] = i
            idx+=1
            counter[i] -= 1

A = [6, 4, 3, 2, 1, 4, 3, 6, 6, 2, 4, 3, 4]
k = 6

#linear
counting_sort(A, k)
print(A)
