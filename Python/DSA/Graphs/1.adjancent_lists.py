class Graph:
    def __init__(self,Nodes):
        self.nodes = Nodes
        self.adjacent_list = {}

        for node in nodes:
            self.adjacent_list[node] = []

    def add_edge(self,u,v):
        self.adjacent_list[u].append(v)
        self.adjacent_list[v].append(u)

    def print_adj_list(self):
        for node in self.nodes:
            print(f"{node} --> {self.adjacent_list[node]}")

nodes = ['A','B','C','D','E','F','G']

graph = Graph(nodes)
graph.add_edge('A','B')
graph.print_adj_list()
