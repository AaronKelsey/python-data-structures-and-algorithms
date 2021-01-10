from collections import deque


def bfs_iterative(graph, start):
    visited = set(start)
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        print(vertex, end=', ')

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return visited


if __name__ == '__main__':
    graph = {'A': ['B', 'C'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F'],
             'D': ['B'],
             'E': ['B', 'F'],
             'F': ['C', 'E']}

    path = bfs_iterative(graph, 'B')
    print(path)
