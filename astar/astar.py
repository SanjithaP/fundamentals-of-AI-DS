import heapq #<-- for making a priortiy heap 

def astar_search(graph, initial_node, goal_node, heuristic_function):
    open_list = []
    closed_set = set()

    start_node = (initial_node, None, 0, heuristic(initial_node))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node, parent, g, h = heapq.heappop(open_list)

        if current_node == goal_node:
            path = []
            while current_node:
                path.insert(0, current_node)
                if parent:
                    current_node, parent, _, _ = parent
                else:
                    current_node = None
            return path

        closed_set.add(current_node)

        for neighbor_node, edge_cost in graph[current_node]:
            if neighbor_node in closed_set:
                continue

            tentative_g = g + edge_cost
            neighbor_heuristic = heuristic(neighbor_node)
            neighbor_entry = (neighbor_node, (current_node, parent, g, h), tentative_g, neighbor_heuristic)
            if neighbor_node not in (node for node, _, _, _ in open_list) or tentative_g < g:
                heapq.heappush(open_list, neighbor_entry)

    return None

#defing the heuristic value
def heuristic(node):
    dictionay = {
        'A':100,
        'B':50,
        'C':110,
        'D':10,
        'E':11,
        'F':0
    }
    return dictionay[node] 

if __name__ == "__main__":
    graph = {
        'A': [('B', 2), ('C', 16)],
        'B': [('D', 3)],
        'C': [('B', 15), ('E', 42)],
        'D': [('C', 12), ('E', 3)],
        'E':[('F',4),('A',28)]
    }
    

    initial_node = 'A'
    goal_node = 'F'
    path = astar_search(graph, initial_node, goal_node, heuristic)
    if path:
        print("Path found:", path)
    else:
        print("Path not found")
