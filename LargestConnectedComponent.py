import numpy as np
from scipy.sparse import csgraph

def LargestConnectedComponent(A):
    ci, sizes = csgraph.connected_components(A, directed=False)
    max_ind = np.argmax(sizes)
    lcc_inds = np.where(ci == max_ind)[0]
    LCC = A[lcc_inds][:, lcc_inds]
    
    return LCC, lcc_inds, ci, sizes

# % LARGESTCONNECTEDCOMPONENT gets the largest connected component of A
# % A is assumed to be undirected.
# %
# % [LCC, lcc_inds, ci, sizes] = LargestConnectedComponent(A) returns
# %   LCC: the largest connected component
# %   lcc_inds: the indices in A corresponding to the connected component
# %   ci: the component indices of the nodes in A
# %   sizes: the sizes of the connected components
