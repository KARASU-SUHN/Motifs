# NLAPLACIAN returns the normalized laplacian of A
import numpy as np
from scipy.sparse import coo_matrix, eye

def nlaplacian(A):
    d = np.sum(A, axis=1)
    d = np.squeeze(np.asarray(d))
    d[d != 0] = 1.0 / np.sqrt(d[d != 0])
    
    i, j, v = coo_matrix(A).row, coo_matrix(A).col, coo_matrix(A).data
    m, n = A.shape
    L = coo_matrix((v * -(d[i] * d[j]), (i, j)), shape=(m, n))
    L = L + eye(n)
    
    return L

