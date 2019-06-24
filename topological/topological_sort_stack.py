from collections import defaultdict

# The Graph Class
class Graph:
	def __init__(self, vertices, directed=True, debug=False):
		self.graph = defaultdict(set)
		self.v = vertices
		self.directed = directed
		self.debug = debug
	def add_edge(self, u, v):
		self.graph[u].add(v)
		if not self.directed:
			self.graph[v].add(u)
	def topo_util(self, v, visited, stack):
		visited[v] = 1 # mark visited
		for i in self.graph[v]:
			if not visited[i]:
				self.topo_util(i, visited, stack)
		stack.insert(0,v) # push to beginning of stack
		if self.debug:
			print("STACK: ",stack)
	def topo_sort(self):
		visited = [0]*self.v
		stack = []
		for i in range(self.v):
			if not visited[i]:
				self.topo_util(i,visited,stack)
		return stack

g = Graph(9, directed=True, debug=True)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 7)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(3, 6)
g.add_edge(3, 4)
g.add_edge(6, 8)

print("Topological Order:\n", g.topo_sort())

