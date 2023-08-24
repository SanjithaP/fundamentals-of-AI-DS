import networkx as nx
import math
import matplotlib.pyplot as plt
explored = []
frontier = []
b = 2 # b=2 for trees
d = 2 #depth of solution
graph = {
    'a': ['b','c'],
    'b': ['d','e'],
    'c': ['f','g'],
    'd': [],
    'e': ['h','i'],
    'f': [],
    'g': [],
    'h': [],
    'i': []}
G = nx.Graph()
for value in graph.keys():
    for i in range(len(graph[value])):
        G.add_edge(value,graph[value][i])
nx.draw(G, with_labels = True, font_weight = 'bold')




explored = set()

def dls(explored, graph, current_state, goal_state, depth_limit):
    if current_state not in explored and depth_limit >= 0:
        if current_state == goal_state:
            print(current_state, end=" ")
            return True
        else:
            print(current_state, end=" ")
        explored.add(current_state)
        if depth_limit > 0:
            found_goal = False
            for adj in graph[current_state]:
                if dls(explored, graph, adj, goal_state, depth_limit - 1):
                    found_goal = True
                    break
            return found_goal
    return False

def depth_limited_search(graph, initial_state, goal_state, depth_limit):
    print("Depth Limited Search:")
    if not dls(explored, graph, initial_state, goal_state, depth_limit):
        print("\nGoal state not found.")


depth_limited_search(graph, 'a','g', 3)
