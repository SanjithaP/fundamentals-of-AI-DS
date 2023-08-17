import networkx as nx
import matplotlib.pyplot as plt

problem = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

explored = []
frontier = []

def bfs(problem,node,explored):
    explored.append(node)
    frontier.append(node)

    while frontier:        
        m = frontier.pop(0)
        print (m, end = " ")

        for child in problem[m]:
            if child not in explored:
                explored.append(child)
                frontier.append(child)
       
print("Following is the Breadth-First Search")
bfs(problem,'5',explored)
