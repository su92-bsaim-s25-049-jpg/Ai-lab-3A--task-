def a_star(graph, start, goal, heuristic):
    open_list = [(start, 0)]  # (node, cost)
    parent = {start: None}
    cost = {start: 0}

    while open_list:
        current, current_cost = open_list.pop(0)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor, value in graph[current]:
            new_cost = cost[current] + value

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                open_list.append((neighbor, new_cost))
                parent[neighbor] = current

    return None

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristic = {
    'A': 7, 'B': 6, 'C': 2,
    'D': 1, 'E': 1, 'F': 0
}

print(a_star(graph, 'A', 'F', heuristic))