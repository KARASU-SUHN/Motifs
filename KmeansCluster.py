import numpy as np
from scipy.sparse import diags
from sklearn.cluster import KMeans
from scipy.sparse.linalg import eigs

def KmeansCluster(A, k):
    Ln = nlaplacian(A)
    eig_opts = {'tol': 1e-6, 'isreal': True, 'issym': True}
    U, _ = eigs(Ln, k, which='SA', **eig_opts)
    D = diags(1.0 / np.sqrt(np.sum(np.abs(U) ** 2, axis=1)))
    T = D.dot(U)
    
    rep = 200  # Number of replications for k-means
    kmeans = KMeans(n_clusters=k, n_init=rep, random_state=0)
    X = kmeans.fit_predict(T)
    
    return X, T
  
# % KMEANSCLUSTER performs a spectral clustering of the (weighted) adjacency
# % matrix A into k clusters using the algorithm in
# % "On Spectral Clustering: Analysis and an algorithm" by Ng et al.
# %
# %  [X, T] = KmeansCluster(A, k) returns
# %    X: the assignment of nodes to the k clusters
# %    T: the embedding of the nodes into R^k used by the algorithm
