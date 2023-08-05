# Q1. Breadth First Traversal for a Graph.

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] 
queue = []     

def bfs(visited, graph, node): #function of BFS
  visited.append(node)
  queue.append(node)

  while queue:          
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling
#-------------------------------------------------------------------------------------------------

#Q2. Depth First Traversal for a Graph-

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() 

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'A')
#---------------------------------------------------------------------------------------------------------

#Q3. Count the number of nodes at given level in a tree using BFS

from collections import deque
  
adj = [[] for i in range(1001)]
  
def addEdge(v, w):
     
    
    adj[v].append(w)
  
    adj[w].append(v)
  
def BFS(s, l):
     
    V = 100
    
    visited = [False] * V
    level = [0] * V
  
    for i in range(V):
        visited[i] = False
        level[i] = 0
        queue = deque()
  
        visited[s] = True
    queue.append(s)
    level[s] = 0
  
    while (len(queue) > 0):
         
        s = queue.popleft()
        
        for i in adj[s]:
            if (not visited[i]):
  
                
                level[i] = level[s] + 1
                visited[i] = True
                queue.append(i)
  
    count = 0
    for i in range(V):
        if (level[i] == l):
            count += 1
             
    return count
  
if __name__ == '__main__':  
    addEdge(0, 1)
    addEdge(0, 2)
    addEdge(1, 3)
    addEdge(2, 4)
    addEdge(2, 5)
  
    level = 2
  
    print(BFS(0, level))

#---------------------------------------------------------------------------------------------------------    
#Q4. Count number of trees in a forest

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)
 
def DFSUtil(u, adj, visited):
    visited[u] = True
    for i in range(len(adj[u])):
        if (visited[adj[u][i]] == False):
            DFSUtil(adj[u][i], adj, visited)
 
def countTrees(adj, V):
    visited = [False] * V
    res = 0
    for u in range(V):
        if (visited[u] == False):
            DFSUtil(u, adj, visited)
            res += 1
    return res
if __name__ == '__main__':
 
    V = 5
    adj = [[] for i in range(V)]
    addEdge(adj, 0, 1)
    addEdge(adj, 0, 2)
    addEdge(adj, 3, 4)
    print(countTrees(adj, V))

#-----------------------------------------------------------------------------------------------------------
# Q5. Detect Cycle in a Directed Graph--

from collections import defaultdict
 
 
class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def isCyclicUtil(self, v, visited, recStack):
 
        visited[v] = True
        recStack[v] = True
 
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
 
        recStack[v] = False
        return False
 
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    if g.isCyclic() == 1:
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain cycle")    