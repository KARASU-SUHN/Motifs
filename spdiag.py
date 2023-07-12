import numpy as np
from scipy.sparse import diags

def spdiag(v):
    D = diags(v, 0, format='csr')
    return D
