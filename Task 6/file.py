# BFS without Queue & without Node

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = []
to_visit = ['A']   # using list instead of queue

while to_visit:
    node = to_visit.pop(0)   # take first element

    if node not in visited:
        print(node)
        visited.append(node)

        for neighbor in graph[node]:
            to_visit.append(neighbor)