import itertools
import networkx as nx
import time

def Motif(graph):
    subgraph_counts = {}

    # Generate all possible combinations of 3 nodes
    node_combinations = itertools.combinations(graph.nodes, 3)

    # Iterate over each combination of nodes
    for combination in node_combinations:
        i, j, k = combination

        # Check if the required edges exist in the graph
        if graph.has_edge(i, j) and graph.has_edge(j, k) and graph.has_edge(k, i):
            # Check if there are no other directed edges between the three nodes
            if not has_additional_edges(graph, i, j, k):
                subgraph = ((i, j), (j, k), (k, i)) #M1
#                 subgraph = ((i, j), (j, k), (k, j), (k, i)) #M2 
#                 subgraph = ((i, j),(j, k),(k, j),(k, i),(i, k)) #M3 
#                 subgraph = ((i, j),(j, i),(j, k),(k, j),(k, i),(i, k)) #M4
#                 subgraph = ((i, j),(j, k),(i, k)) #M5
#                 subgraph = ((j, i),(j, k),(i, k),(k, i)) #M6
#                 subgraph = ((i, j),(k, j),(i, k),(k, i)) #M7 
                subgraph_counts[subgraph] = subgraph_counts.get(subgraph, 0) + 1

    return subgraph_counts

def has_additional_edges(graph, i, j, k):
    # Check if there are any other directed edges between the three nodes
    for u, v in graph.edges:
        if (u, v) != (i, j) and (u, v) != (j, k) and (u, v) != (k, i): #M1
#         if (u, v) != (i, j) and (u, v) != (j, k) and (u, v) != (k, j) and (u, v) != (k, i): #M2
#         if (u, v) != (i, j) and (u, v) != (j, k) and (u, v) != (k, j) and (u, v) != (k, i) and (u, v) != (i, k): #M3
#         if (u, v) != (i, j) and (u, v) != (j, i) and (u, v) != (j, k) and (u, v) != (k, j) and (u, v) != (k, i) and (u, v) != (i, k): #M4
#         if (u, v) != (i, j) and (u, v) != (j, k) and (u, v) != (i, k): #M5
#         if (u, v) != (j, i) and (u, v) != (j, k) and (u, v) != (i, k) and (u, v) != (k, i): #M6
#         if (u, v) != (i, j) and (u, v) != (k, j) and (u, v) != (i, k) and (u, v) != (k, i): #M7
            if u in (i, j, k) and v in (i, j, k):
                return True
    return False

# Example usage
# Create a directed graph using networkx
graph = nx.DiGraph()

# Add edges to the graph

with open('s.txt', 'r') as file:
    for line in file:
        data = line.split()
        node1 = int(data[0])
        node2 = int(data[1])
        sign = int(data[2])
        graph.add_edge(node1, node2, sign=sign)


start_time = time.time()
subgraph_counts = Motif(graph)
end_time = time.time()

total_count = sum(subgraph_counts.values())

# Write the output to a text file
output_file = "m1.txt"
with open(output_file, 'w') as file:
    file.write("Found Subgraphs:\n")
    for subgraph, count in subgraph_counts.items():
        file.write(f"{subgraph} -> Count: {count}\n")

    file.write(f"\nTotal Count: {total_count}\n")
    file.write(f"Execution time: {end_time - start_time} seconds\n")

print(f"Output saved to {output_file}")


# # Print the found subgraphs and their counts
# for subgraph, count in subgraph_counts.items():
#     print(subgraph, "-> Count:", count)
    
# print("Total Count:", total_count)

# # Print the execution time
# print("Execution time:", end_time - start_time, "seconds")
