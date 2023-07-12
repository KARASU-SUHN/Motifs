import numpy as np
from scipy.sparse import eye
from scipy.sparse.linalg import eigs

def nfiedler(A, tol=1e-12):
    L = nlaplacian(A)
    n = A.shape[0]
    V, lambdas = eigs(L + eye(n), k=2, which='SA', tol=tol)
    eig_order = np.argsort(np.diag(lambdas))
    ind = eig_order[-1]
    x = V[:, ind]
    x = x / np.sqrt(np.sum(A, axis=1))
    lam = lambdas[ind, ind] - 1
    
    return x, lam

# % NFIEDLER returns the fiedler vector of the normalized laplacian of A.
