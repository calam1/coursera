# https://www.python.org/doc/essays/graphs/

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

def find_path(graph, start, end, path=[]):
    #print(path)
    path = path + [start]

    if start == end:
        return path

    if not start in graph:
        return None

    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath

    return None

print('find path {}'.format(find_path(graph, 'A', 'D')))

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return [path]

    if not start in graph:
        return []

    paths = []

    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths

print('find all paths {}'.format(find_all_paths(graph, 'A', 'D')))

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return path

    if not start in graph:
        return None

    shortest = None

    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath

    return shortest

print('find shortest path {}'.format(find_shortest_path(graph, 'A', 'D')))



graph2 = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

graph3 = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# cyclical graph
def depth_first_search(graph, start): # dictionary set
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited) # subtraction is overloaded, just removes element
    return visited

print('depth first search {}'.format(depth_first_search(graph2, 'A')))

# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# cyclical graph
def depth_first_search_recursive(graph, start, visited=None): # dictionary set
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        depth_first_search_recursive(graph, next, visited)
    return visited

print('depth first search recursive {}'.format(depth_first_search_recursive(graph2, 'A')))


def depth_first_search_list(graph, start, path=[]): # dictionary array
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return path

print('depth first search list {}'.format(depth_first_search_list(graph3, 'A')))

# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
def breadth_first_search(graph, start): # dictionary set
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

print('breadth first search {}'.format(breadth_first_search(graph2, 'A')))

# http://code.activestate.com/recipes/576723-dfs-and-bfs-graph-traversal/
def breadth_first_search_2(graph, start, path=[]): # dictionary array
  stack = [start]
  while stack:
    visited = stack.pop(0)
    if not visited in path:
      path=path+[visited]
      stack = stack + graph[visited]
  return path

print('breadth first search 2 {}'.format(breadth_first_search_2(graph3, 'A')))
