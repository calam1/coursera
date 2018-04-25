d = {}

def find(x, y):
    ''' find total number of paths from (0, 0) to whatever the inputted x and y is'''
    if x == 0 and y == 0: # means you have arrived at endpoint
        return 1
    if x < y:
        return 0
    if  d.get((x, y)) is not None:
        return d.get((x, y))
    ret = 0
    if x > 0:
        ret += find(x-1, y)
    if y > 0:
        ret += find(x, y-1)
    if x > 0 and y > 0:
        ret += find(x-1, y-1)
    d[(x, y)] = ret

    return ret

def find_rec(x, y):
    if x == 0 or y == 0:
        return 1
    return find_rec(x-1, y) + find_rec(x, y-1)

def find_dp(x, y):
    solution = [[0 for i in range(x+1)] for j in range(y+1)]

    for i in range(x+1):
        for j in range(y+1):
            if i == 0 or j == 0:
                solution[i][j] = 1
            else:
                solution[i][j] = solution[i-1][j] + solution[i][j-1]

    return solution[x][y]



print('find dp 1 {} '.format(find(2, 2)))
print('find dp 2 {}'.format(find_dp(2, 2)))
print('find recursive {}'.format(find_rec(2, 2)))
