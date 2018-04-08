# Uses python3

n = int(input())
a = [int(x) for x in input().split()]

assert(len(a) == n)

largest = max(a)
a.remove(largest)
second_largest = max(a)

print(largest * second_largest)

#for i in range(0, n):
#    for j in range(i+1, n):
#        if a[i]*a[j] > result:
#            result = a[i]*a[j]
#
#print(result)
