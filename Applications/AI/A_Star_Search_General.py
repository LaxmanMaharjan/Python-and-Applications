# This class represent a graph
class Graph:
    # Initialize the class
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()
    # Create an undirected graph by adding symmetric edges
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist
    # Add a link from A and B of given distance, and also add the inverse link if the graph is undirected
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance
    # Get neighbors or a neighbor
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)
    # Return a list of nodes in the graph
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)
        
# This class represent a node
class Node:
    # Initialize the class
    def __init__(self, name:str, parent:str):
        self.name = name
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost
    # Compare nodes
    def __eq__(self, other):
        return self.name == other.name
    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.name, self.f))
# A* search
def astar_search(graph, heuristics, start, end):
    
    # Create lists for open nodes and closed nodes
    open = []
    closed = []
    # Create a start node and an goal node
    start_node = Node(start, None)
    goal_node = Node(end, None)
    # Add the start node
    open.append(start_node)
    
    # Loop until the open list is empty
    while len(open) > 0:
        # Sort the open list to get the node with the lowest cost first
        open.sort()
        # Get the node with the lowest cost
        current_node = open.pop(0)
        # Add the current node to the closed list
        closed.append(current_node)
        
        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name + ': ' + str(current_node.g))
                current_node = current_node.parent
            path.append(start_node.name + ': ' + str(start_node.g))
            # Return reversed path
            return path[::-1]
        # Get neighbours
        neighbors = graph.get(current_node.name)
        # Loop neighbors
        for key, value in neighbors.items():
            # Create a neighbor node
            neighbor = Node(key, current_node)
            # Check if the neighbor is in the closed list
            if(neighbor in closed):
                continue
            # Calculate full path cost
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.g + neighbor.h
            # Check if neighbor is in open list and if it has a lower f value
            if(add_to_open(open, neighbor) == True):
                # Everything is green, add neighbor to open list
                open.append(neighbor)
    # Return None, no path is found
    return None
# Check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f > node.f):
            return False
    return True
    
# The main entry point for this module
def main():
    # Create a graph
    graph = Graph()
    # Create graph connections (Actual distance)
    graph.connect('A', 'B', 101)
    graph.connect('A', 'C', 98)
    graph.connect('A', 'E', 110)
    graph.connect('B', 'D', 112)
    graph.connect('E', 'F', 232)
    graph.connect('E', 'G', 200)
    graph.connect('F', 'H', 242)
    graph.connect('G', 'I', 300)
    graph.connect('H', 'I', 101)
		
    # Make graph undirected, create symmetric connections
    graph.make_undirected()
    # Create heuristics (straight-line distance, air-travel distance)
    heuristics = {}
    heuristics['A'] = 366
    heuristics['B'] = 374
    heuristics['C'] = 329
    heuristics['D'] = 244
    heuristics['E'] = 253
    heuristics['F'] = 178
    heuristics['G'] = 193
    heuristics['H'] = 98
    heuristics['I'] = 0
    # Run the search algorithm
    path = astar_search(graph, heuristics, 'A', 'I')
    print("Solution of Question1:")
    print(path)
    print(f"Total Cost: {path[-1].split(' ')[-1]}")
    print("------" * 20)
    graph1 = Graph()
    # Create graph connections (Actual distance)
    graph1.connect('A', 'B', 2)
    graph1.connect('A', 'C', 1)
    graph1.connect('A', 'S', 1)
    graph1.connect('B', 'D', 5)
    graph1.connect('C', 'D', 3)
    graph1.connect('C', 'G', 4)
    graph1.connect('D', 'G', 2)
    graph1.connect('S', 'G', 10)

    # Make graph undirected, create symmetric connections
    graph1.make_undirected()
    # Create heuristics (straight-line distance, air-travel distance)
    heuristics1 = {}
    heuristics1['S'] = 5
    heuristics1['A'] = 3
    heuristics1['B'] = 4
    heuristics1['C'] = 2
    heuristics1['D'] = 6
    heuristics1['G'] = 0

    path1 = astar_search(graph1, heuristics1, 'S', 'G')
    print("Solution of Question2:")
    print(path1)
    print(f"Total Cost: {path1[-1].split(' ')[-1]}")
    print("------" * 20)
    graph2 = Graph()
    # Create graph connections (Actual distance)
    graph2.connect('S', 'B', 4)
    graph2.connect('S', 'C', 3)
    graph2.connect('F', 'B', 5)
    graph2.connect('E', 'B', 12)
    graph2.connect('C', 'D', 7)
    graph2.connect('C', 'E', 10)
    graph2.connect('D', 'E', 2)
    graph2.connect('G', 'E', 5)
    graph2.connect('F', 'G', 16)

    # Make graph undirected, create symmetric connections
    graph2.make_undirected()
    # Create heuristics (straight-line distance, air-travel distance)
    heuristics2 = {}
    heuristics2['S'] = 14
    heuristics2['B'] = 12
    heuristics2['C'] = 11
    heuristics2['D'] = 6
    heuristics2['E'] = 4
    heuristics2['F'] = 11
    heuristics2['G'] = 0

    path2 = astar_search(graph2, heuristics2, 'S', 'G')
    print("Solution of Question3:")
    print(path2)
    print(f"Total Cost: {path2[-1].split(' ')[-1]}")
    print("------" * 20)
# Tell python to run main method
if __name__ == "__main__":
    main()
