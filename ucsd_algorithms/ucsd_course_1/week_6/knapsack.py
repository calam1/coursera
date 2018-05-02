# Uses python3
import sys

def recursive_optimal_weight(capacity, stuff, m):
    # write your code here
    #print('capacity {}'.format(capacity))
    #print('stuff {}'.format(stuff))

    if capacity <= 0: return 0
    if m <= 0: return 0

    if stuff[m - 1] <= capacity:
        return max(recursive_optimal_weight(capacity, stuff, m - 1),
                   stuff[m - 1] + recursive_optimal_weight(capacity - stuff[m - 1] , stuff, m - 1))
    else:
        return recursive_optimal_weight(capacity, stuff, m - 1)


def optimal_weight(capacity, stuff):
    solution = [[0 for _ in range(len(stuff)+1)] for _ in range(capacity+1)]

    for i in range(capacity+1):
        for j in range(len(stuff)+1):
            if i == 0 or j == 0:
                solution[i][j] = 0
            else:
                if stuff[j-1] <= i:
                    solution[i][j] = max(solution[i][j-1],
                                         stuff[j-1] + solution[i - stuff[j-1]][j-1])
                else:
                    solution[i][j] = solution[i][j-1]

    return solution[capacity][len(stuff)]

#print('recursive {}'.format(recursive_optimal_weight(10, [1, 4, 8], 3)))
#print('dynamic program {}'.format(optimal_weight(10, [1, 4, 8])))



if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
    #print(recursive_optimal_weight(W, w, len(w)))
