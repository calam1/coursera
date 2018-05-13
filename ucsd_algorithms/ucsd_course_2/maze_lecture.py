grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 2]]

# https://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/
def search(x, y):
    if grid[x][y] == 2:
        return True
    elif grid[x][y] == 1:
        return False
    elif grid[x][y] == 3:
        return False
    else:
        grid[x][y] = 3

    if ((x < len(grid)-1 and search(x+1, y))
        or (y < len(grid)-1 and search(x, y+1))
        or (x > 0 and search(x-1, y))
        or (y > 0 and search(x, y-1))):
        return True

    return False

print(search(0, 0))