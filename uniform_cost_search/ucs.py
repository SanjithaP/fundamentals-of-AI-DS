import heapq

def uniform_cost_search(graph, start, goal):
    queue = [(0, start)]  # Priority queue to keep track of nodes to visit
    visited = set()       # Set to keep track of visited nodes

    while queue:
        cost, node = heapq.heappop(queue)  # Pop node with the lowest cost
        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return cost

        for neighbor, neighbor_cost in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + neighbor_cost, neighbor))

    return float('inf')  # No path found

# Example graph represented as a dictionary of dictionaries
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
goal_node = 'D'
result = uniform_cost_search(graph, start_node, goal_node)
print(f"Shortest path cost from {start_node} to {goal_node}: {result}")
