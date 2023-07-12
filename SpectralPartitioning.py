import numpy as np

def SpectralPartitioning(A):
    part_vec, _ = nfiedler(A)
    order = np.argsort(part_vec)
    
# % Compute the conductance values (vectorized)
    B = A[order, :][:, order]
    B_lower = np.tril(B)
    B_sums = np.sum(B, axis=1)
    B_lower_sums = np.sum(B_lower, axis=1)
    volumes = np.cumsum(B_sums)
    num_cut = np.cumsum(B_sums - 2 * B_lower_sums)
    total_vol = np.sum(A)
    volumes_other = total_vol * np.ones(len(order)) - volumes
    vols = np.minimum(volumes, volumes_other)
    scores = num_cut / vols
    scores = scores[:-1]

    condc, min_ind = np.min(scores), np.argmin(scores)
  
# % The output cluster is the smaller of the two sides of the partition
    n = A.shape[0]
    if min_ind <= np.floor(n / 2):
        cluster = order[:min_ind]
    else:
        cluster = order[min_ind + 1:]

    condv = np.minimum(scores, scores[::-1])
    condv = condv[:int(np.ceil(len(scores) / 2))]

    return cluster, condv, condc, order

# % SPECTRALPARTITIONING performs a spectral partitioning of A and
# % returns several relevant quantities.  It assumes that A is undirected
# % and connected.
# %
# %  [order, condv, comm, condc] = SpectralPartitioning(A) returns
# %   cluster: vector of nodes in the smaller side of the partition
# %   condv: the sweep conductance vector
# %   condc: the conductance of the cluster
# %   order: the spectral ordering
