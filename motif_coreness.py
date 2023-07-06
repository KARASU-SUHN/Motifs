import itertools
import networkx as nx
import time
import csv

def load_coreness(file_path):
    coreness = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            node, core = map(int, row)
            coreness[node] = core
    return coreness


def find_special_subgraphs(graph, coreness):
    coreness_counts = {}

    # Generate all possible combinations of 3 nodes
    node_combinations = itertools.combinations(graph.nodes, 3)

    # Iterate over each combination of nodes
    for combination in node_combinations:
        i, j, k = combination

        # Check if the required edges exist in the graph
        if graph.has_edge(i, j) and graph.has_edge(j, k) and graph.has_edge(i, k):
            # Check if there are no additional edges between the three nodes
            if not has_additional_edges(graph, i, j, k):
                # Check if the coreness values satisfy the condition
                if coreness[i] > coreness[j] > coreness[k]:
                    coreness_value = coreness[i]
                    subgraph = ((i, j), (j, k), (i, k))

                    if coreness_value in coreness_counts:
                        coreness_counts[coreness_value]['count'] += 1
                        coreness_counts[coreness_value]['subgraphs'].append(subgraph)
                    else:
                        coreness_counts[coreness_value] = {'count': 1, 'subgraphs': [subgraph]}

    return coreness_counts

def has_additional_edges(graph, i, j, k):
    # Check if there are any additional directed edges between the three nodes
    for u, v in graph.edges:
        if (u, v) != (i, j) and (u, v) != (j, k) and (u, v) != (i, k):
            if u in (i, j, k) and v in (i, j, k):
                return True
    return False


# Load the coreness data
coreness = load_coreness('coreness.csv')

# Create a directed graph using networkx
graph = nx.DiGraph()

# Load the edges from the graph file
with open('data.txt', 'r') as file:
    for line in file:
        u, v, weight = line.strip().split('\t')
        graph.add_edge(int(u), int(v), weight=int(weight))

start_time = time.time()
coreness_counts = find_special_subgraphs(graph, coreness)
end_time = time.time()

print("Subgraph Counts based on Coreness:")
for coreness_value, count_info in sorted(coreness_counts.items()):
    subgraph_count = count_info['count']
    subgraphs = count_info['subgraphs']
    print(f"Coreness {coreness_value} -> Subgraph Count: {subgraph_count}")
    for subgraph in subgraphs:
        print("Subgraph:", subgraph)
    print()

print("Execution time:", end_time - start_time, "seconds")
