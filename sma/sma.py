Google Classroom
Classroom
AI & DS
2023-odd
Home
Calendar
Enrolled
To-do
C
CSE101 PROBLEM SOLVING & PROGRAMMING IN C - SEC I1 OCT2021
I1
N
NATURAL LANGUAGE PROCESSING
AIDS (Odd 23-24)
2
2023-24 Odd_CSE308 Operating Systems
F Section
C
CSE303: Computer Networks Laboratory
AIDS-F | Sem-5 | SoC Lab-3
A
AI & DS
2023-odd
C
CSE302-CN
P
PA&DV
F
C
CSE305&306DAA_2023
E
R
RM-DS -2023 - AI&DS
F
C
CSE304_Python_AIDS_F_2023
F
E
EIE101R01
I1
C
CSE103 & 104 G 2022
J
Java - 2022
A &G
M
MEC102 2nd Sem 2022
E1
C
CSE201 Object Oriented Programming in C++
E1
Archived classes
Settings
Stream
Classwork
People
AI & DS 2023-odd
AI & DS
2023-odd
Upcoming
Woohoo, no work due soon!

Announce something to your class

Post by Mukesh Prasanna
Mukesh Prasanna
Created Sep 14Sep 14
Genetic Algorithm

geneticlago.py
Text

Add class comment…


Post by Subrahmanya
Subrahmanya
Created Sep 12Sep 12
visualizing simulated annealing

simAnnVis.ipynb
Binary File

Add class comment…

Material: "Unit 1"
Prof. PRADEEPA. S posted a new material: Unit 1
Created Sep 5Sep 5 (Edited Sep 5)

Post by Mukesh Prasanna
Mukesh Prasanna
Created Sep 2Sep 2
SMA star

Input.txt
Text

sma.py
Text

Add class comment…


Post by Mudit Golchha
Mudit Golchha
Created Sep 2Sep 2
A STAR

Mudit_aids3_astar.ipynb
Binary File

Add class comment…


Announcement: "see"
Prof. PRADEEPA. S
Created Sep 2Sep 2
see

Local search.pptx
PowerPoint

Add class comment…


Post by Manikandan R
Manikandan R
Created Aug 22Aug 22
Greedy Best First Search

Greedy Best First Search.ipynb
Binary File

Add class comment…


Post by Mudit Golchha
Mudit Golchha
Created Aug 22Aug 22
A* search
Displaying 22 Aug 2023 at 10:41.jpg
22 Aug 2023 at 10:41.jpg

Add class comment…


Post by Karthik Narayan Mohan
Karthik Narayan Mohan
Created Aug 17Aug 17
BFS, DFS, DLS, Uniform Cost Search, 

Iterative Deepening Search

SearchingAlgorithms.ipynb
Binary File

Add class comment…


Post by Swarathmica S
Swarathmica S
Created Aug 8Aug 8
best first search

v=int(input('Enter the number of vertices: '))
graph = [[] for i in range(v)]
def bfs(s,g,n):
    vis=[False]*n
    o,c=[],[]
    o.append((0,s))
    vis[s]=True
    while len(o)>0:
        node=o.pop()[1]
        c.append(node)
        print(node)
        if node==g:
            return
        for k,c1 in graph[node]:
            if vis[k]==False:
                vis[k]==True
                o.append((c1,k))
        if len(o)>0:
            o.sort(key = lambda x: x[1])

 
def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))
edge=int(input('no.of edges:'))
for i in range(edge):
    x=int(input('vertex 1:'))
    y=int(input('vertex 2:'))
    c=int(input('cost: '))
    addedge(x,y,c)
source=int(input('source '))
goal=int(input('goal  '))
bfs(source,goal,v)
#print(graph[0])

Add class comment…


Announcement: "for BFS"
Prof. PRADEEPA. S
Created Aug 8Aug 8
for BFS

LAB2.pptx
PowerPoint

Add class comment…


Post by Mukesh Prasanna
Mukesh Prasanna
Created Aug 3Aug 3
BFS and DFS

GraphSearch.py
Text

Add class comment…


Post by Karthik Narayan Mohan
Karthik Narayan Mohan
Created Aug 3Aug 3
Code for BFS and DFS:
import networkx as nx
import matplotlib.pyplot as plt
visited = []
queue = []

graph = {
    'a': ['b','c'],
    'b': ['d','e'],
    'c': ['f','g'],
    'd': [],
    'e': [],
    'f': [],
    'g': []
}
G = nx.Graph()
for value in graph.keys():
    for i in range(len(graph[value])):
        G.add_edge(value,graph[value][i])
nx.draw(G, with_labels = True)


def bfs(visited,graph,source):
    visited.append(source)
    queue.append(source)
    while queue:
        element = queue.pop(0)
        print(element, end = " ")
        for adj in graph[element]:
            if adj not in visited:
                visited.append(adj)
                queue.append(adj)
print("Breadth First Search: ")
bfs(visited,graph,'a')

visited = set()
def dfs(visited,graph,source):
    if source not in visited:
        print(source, end = " ")
        visited.add(source)
        for adj in graph[source]:
            dfs(visited,graph,adj)
print("Depth First Search: ")
dfs(visited,graph,'a')

Add class comment…


Post by Mukesh Prasanna
Mukesh Prasanna
Created Aug 3Aug 3
Without Queue class

import networkx as nx
import matplotlib.pyplot as plt

class Graph :

    def __init__(self) :
        self.graph = {}
        self.visual = []
        self.visualDFS = []
        self.visualBFS = []

    def addEdge(self, u, v) :
        self.visual.append([u,v])
        if u in self.graph :
            self.graph[u].append(v)
        else :
            self.graph[u] = [v]
        self.visited = []

   
    def BFS(self, s) :
        queue = []
        self.visited.append(s)
        queue.append(s)
        print("BFS Traversal")
        while queue :
            vert = queue.pop(0)
            self.visualBFS.append(vert)
            print(vert, end = "  ")
            for i in self.graph[vert] :
                if i not in self.visited :
                    queue.append(i)
                    self.visited.append(i)

    def DFSvisit(self, v, visited) :
       
        visited[v] = True
        print(v, end = "  ")
        self.visualDFS.append(v)
       
        for i in self.graph[v] :
            if visited[i]==False :
                self.DFSvisit(i, visited)
       

    def DFS(self) :
        print("\nDFS Traversal")
        vertices = len(self.graph)
        visited = [False]*vertices
        for i in range(vertices) :
            if visited[i]==False :
                self.DFSvisit(i, visited)
           

    def visualize(self) :
        g1 = nx.Graph()
        g1.add_edges_from(self.visual)
        nx.draw_networkx(g1)
        plt.show()
   
    def visualizeBFS(self) :
        plt.clf()
        g2 = nx.Graph()
        for i in range(len(self.visualBFS)-1) :
            g2.add_edge(self.visualBFS[i], self.visualBFS[i+1])
        nx.draw_networkx(g2)
        plt.show()

    def visualizeDFS(self) :
        plt.clf()
        g3 = nx.Graph()
        for i in range(len(self.visualDFS)-1) :
            g3.add_edge(self.visualDFS[i], self.visualDFS[i+1])
        nx.draw_networkx(g3)
        plt.show()


g = Graph()
for _ in range(int(input("Enter the number of edges : "))) :
    u, v = map(int, input('Enter the start and end vertex : ').split())
    g.addEdge(u, v)

source = int(input('Enter the source vertex : '))

g.BFS(source)
g.DFS()
   
g.visualize()

g.visualizeBFS()

g.visualizeDFS()

Add class comment…


Announcement: "https://meet.google.com/jyt-mvso-fwt…"
Prof. PRADEEPA. S
Created Aug 1Aug 1
https://meet.google.com/jyt-mvso-fwt


LAB: 1 to 3

Add class comment…


Post by Nitin Shriram S
Nitin Shriram S
Created Jul 31Jul 31
WhatsApp link for G

https://chat.whatsapp.com/Jr4jilTW7W1KpidECKkApp

Add class comment…


Post by Mudit Golchha
Mudit Golchha
Created Jul 31Jul 31
WhatsApp link for f section

https://chat.whatsapp.com/EHoYluLMUZkCaEhxMPLtAc

Add class comment…

from collections import defaultdict

class Graph :
    def __init__(self) -> None:
        self.edges = defaultdict(dict)
        self.nodes = defaultdict(int)

    def addNode(self, x, hval) :
        self.nodes[x] = hval 
    
    def addEdge(self, u, v, w) :
        self.edges[u][v] = w

    def calcCost(self, cost, path) :
        return cost-self.nodes[path[-2]] + self.edges[path[-2]][path[-1]] + self.nodes[path[-1]]
    
    def smastar(self, source, goal, bound) :

        if source==goal :
            print(source)
            return
        
        if bound==1 :
            print('Goal not found')
            return
        
        bound+=1
        
        frontier = []
        frontier.append((self.nodes[source], (source,)))

        visited = defaultdict(list)
        mem = 1

        while frontier :
            
            if mem==bound :
                frontier.pop(-1)
                mem-=1
            
            if not frontier :
                print('Failure')
                return
            
            cost, path = frontier.pop(0)
            added = False
            for i in self.edges[path[-1]] :
                if i not in visited[path[-1]] :
                    npath = path+(i,)
                    ncost = self.calcCost(cost, npath)
                    frontier.append((ncost, npath))
                    visited[path[-1]].append(i)
                    mem+=1
                    added = True
                    if mem==bound :
                        break 
                
            
            if not added :
                print('Failure')
                return
            
            frontier.sort()
            if frontier[0][1][-1]==goal :
                print('Path :', frontier[0][1])
                print('Cost :', frontier[0][0])
                return 
            


g = Graph()

for _ in range(int(input('Enter the number of nodes : '))) :
    x, hval = input('Enter the node and heuristic value : ').split()
    g.addNode(x, int(hval))
    
for _ in range(int(input('\nEnter the number of edges : '))) :
    u,v,w = input('Enter the source and destination of edge : ').split()
    g.addEdge(u,v,int(w))
    
source, goal = input('Enter the source and goal nodes : ').split()
bound = int(input('Enter memory bound : '))
g.smastar(source, goal, bound)

            
            
            
            



