#python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    solution = {}
    for i in a:
       solution[i] = 1 if i not in solution else solution[i] + 1 

    #print('solution {}'.format(solution))

    for key, value in solution.items():
        if value > right // 2:
            #print('greater than equal')
            return 1

    return -1 

# this does not handle not finding majority, one does not exist that is
def get_majority_element_divide_conquer(array):
    if len(array) == 0:
        return -1
    if len(array) == 1:
        return array[0]

    a_array = array[:len(array)//2]
    b_array = array[len(array)//2:]
    a = get_majority_element_divide_conquer(a_array)
    b = get_majority_element_divide_conquer(b_array)

    if a == b: 
        return a
    else:
        return a if array.count(a) > len(array)//2 else b



def get_majority_element_naive(a):
    for i in range(len(a)):
        current = a[i]
        count = 0
        for j in range(len(a)): 
            if a[j] == current:
                count += 1
        if count > n//2:
            return a[i]
    return -1
    


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #print('n {}'.format(n))
    #print('a {}'.format(a))
    if get_majority_element(a) != -1:
    #if get_majority_element_naive(a) != -1:
        print(1)
    else:
        print(0)

