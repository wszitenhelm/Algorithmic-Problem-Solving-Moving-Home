import sys
import time

# This class creates Graph object and have all essential methods 
class Graph(object):
    def __init__(self, nodes, people, chains):
        self.nodes = nodes
        self.people = people
        self.chains = chains 
        self.graph = self.empty_graph(nodes)
        
    def empty_graph(self, nodes):
        # Contructs empty dictionaries for all nodes
        graph = {}
        for node in nodes:
            graph[node] = {}
        return graph
    
    def add_edge(self, v, u, value):
        # Adds edge with value between two nodes 
        self.graph[v][u] = value
        
    def get_nodes(self):
        # Returns all the nodes of the graph.
        return self.nodes

    def value(self, node1, node2):
        # Returns the value of an edge between two nodes.
        if node1 == "s":
            return self.graph[node1][node2]
        else:
            return self.graph[node1][node2]

    def get_edges(self, node):
        # Returns the neighbours of a node.
        neighbours = []
        for node_to in self.nodes:
            if self.graph[node].get(node_to, False) != False:
                neighbours.append(node_to)
        return neighbours
    
# Main program of this task that at the beginning reads the input 
def main():
    lines=sys.stdin.readlines()
    l=lines[0].split()
    no_chains=int(l[0])
    no_people=int(l[1])
    no_options = len(lines)
    nodes = []
    nodes.append("s")
    # Program goes through the input and creates nodes 
    for i in range(1, no_options):
        values = lines[i].split()
        val_1a = values[0]
        val_1b = values[1]
        val_2a = values[2]
        val_2b = values[3]
        val_12 = values[4]
        if str(val_1a+val_1b) not in nodes:
            nodes.append(str(val_1a+val_1b))
    # Program creates graph with nodes from the input 
    graph = Graph(nodes, no_people, no_chains)
    # Program once again goes through the input to search for edges
    # and when finds them adds them to the graph.
    for i in range(1, no_options):
        values = lines[i].split()
        val_12 = int(values[4])
        node_a = str(values[0]+values[1])
        node_b = str(values[2]+values[3])
        if node_a == node_b:
            graph.add_edge(node_a, node_a, val_12)
            if node_a[1] == "0":
                graph.add_edge("s", node_b, val_12)
            else:
                to_change = int(node_a[-1]) - 1
                node_before = node_a[0] + str(to_change)
                graph.add_edge(node_before, node_b, val_12)
        else:
            graph.add_edge(node_a, node_b, val_12)


    # Updating edges values 
    for node in graph.nodes:
        nh = graph.get_edges(node)
        for n in nh:
            if node != n and node != "s":
                if node[0] != n[0]:
                    value_curr = graph.value(node, n)
                    to_add = graph.value(n, n)
                    graph.add_edge(node, n, value_curr+to_add)


    memo = {}

    shortest_way = shortest_time(graph, "s", no_people, memo)
    print(shortest_way)

def shortest_time(graph, curr_node, i, memo):
    if curr_node[-1] == str(graph.people - 1):
        return 0
    else:
        next_nodes = []    
        for node in graph.nodes:
            if node != "s":
                if int(node[1]) == graph.people - i:
                    next_nodes.append(node)
        
        minimum = sys.maxsize
        for node in next_nodes:
            if node in memo:
                val = memo[node] + graph.value(curr_node, node)
            else:
                short_time = shortest_time(graph, node, i-1, memo)
                val = short_time + graph.value(curr_node, node)
                memo[node] = short_time          

            if val < minimum:
                minimum = val
                
        return minimum


start = time.time()
main()
end = time.time()
total = end - start
print(f"time: {total}")

















               

