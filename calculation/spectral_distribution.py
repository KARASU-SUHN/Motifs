import os
import numpy as np
import matplotlib.pyplot as plt


def read_signed_edges_from_file(file_path):
    signed_edges = []
    max_node = -1  # To track the maximum node index
    with open(file_path, 'r') as file:
        for line in file:
            i, j, sign = map(int, line.strip().split())
            signed_edges.append((i, j, sign))
            max_node = max(max_node, i, j)  # Update max_node with the maximum node index
    num_nodes = max_node + 1
    return signed_edges, num_nodes

def compute_adjacency_matrix(signed_edges, num_nodes):
    adjacency_matrix = np.zeros((num_nodes, num_nodes))

    for edge in signed_edges:
        i, j, sign = edge
        adjacency_matrix[i - 1][j - 1] = sign  # Assuming 1-based node indexing
        adjacency_matrix[j - 1][i - 1] = sign  # Assuming an undirected graph

    return adjacency_matrix

def calculate_spectral_distribution(adjacency_matrix):
    eigenvalues = np.linalg.eigvals(adjacency_matrix)
    return np.sort(eigenvalues)

def calculate_cdf(spectral_distribution):
    n = len(spectral_distribution)
    probabilities = np.arange(1, n + 1) / n
    return spectral_distribution, probabilities

def visualize_spectral_distribution_cdf(spectral_distribution, probabilities, file_name):
    plt.plot(spectral_distribution, probabilities, marker='o', linestyle='-')
    plt.title(f"Spectral Distribution CDF of the Adjacency Matrix ({file_name})")
    plt.xlabel("λ (Eigenvalues)")
    plt.ylabel("P(x <= λ)")
    plt.grid(True)
    plt.show()

# Example usage for reading from the TXT file and visualizing the spectral distribution (CDF):
file_path = '/filepath.txt'

signed_edges, num_nodes = read_signed_edges_from_file(file_path)
adjacency_matrix = compute_adjacency_matrix(signed_edges, num_nodes)
spectral_distribution = calculate_spectral_distribution(adjacency_matrix)
eigenvalues, probabilities = calculate_cdf(spectral_distribution)

# Get the file name without the extension
file_name = os.path.splitext(os.path.basename(file_path))[0]

visualize_spectral_distribution_cdf(eigenvalues, probabilities, file_name)
