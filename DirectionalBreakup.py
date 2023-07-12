import numpy as np
from scipy.sparse import csc_matrix

def DirectionalBreakup(A):
    # Set non-zero elements to 1
    A[A != 0] = 1
    
    # Bidirectional subgraph
    B = csc_matrix((A.multiply(A.T) != 0).astype(int))
    
    # Unidirectional subgraph
    U = A - B
    
    # Undirected graph
    G = A | A.T
    
    return B, U, G

# % DIRECTIONALBREAKUP returns the bidirectional, unidirectional, and
# % undirected versions of the adjacency matrix A.
# %
# % [B, U, G] = DirectionalBreakup(A) returns
# %   B: the bidirectional subgraph
# %   U: the unidirectional subgraph
# %   G: the undirected graph
# %
# %  Note that G = B + U
