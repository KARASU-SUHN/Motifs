import numpy as np
from scipy.sparse import csr_matrix
from DirectionalBreakup import directional_breakup

def MotifAdjacency(A, motif):
    # Ignore diagonals and weights
    A = A - csr_matrix((A.diagonal(), (np.arange(A.shape[0]), np.arange(A.shape[0]))), shape=A.shape)
    A.data = np.minimum(A.data, 1)
    
    lmotif = motif.lower()
    if lmotif == 'm1':
        W = M1(A)
    elif lmotif == 'm2':
        W = M2(A)
    elif lmotif == 'm3':
        W = M3(A)
    elif lmotif == 'm4':
        W = M4(A)
    elif lmotif == 'm5':
        W = M5(A)
    elif lmotif == 'm6':
        W = M6(A)
    elif lmotif == 'm7':
        W = M7(A)
    elif lmotif == 'm8':
        W = M8(A)
    elif lmotif == 'm9':
        W = M9(A)
    elif lmotif == 'm10':
        W = M10(A)
    elif lmotif == 'm11':
        W = M11(A)
    elif lmotif == 'm12':
        W = M12(A)
    elif lmotif == 'm13':
        W = M13(A)
    elif lmotif == 'bifan':
        W = Bifan(A)
    elif lmotif == 'edge':
        _, _, W = DirectionalBreakup(A)
    else:
        raise ValueError("Unknown motif " + motif)
    
    return W


def M1(A):
    _, U, _ = DirectionalBreakup(A)
    C = U.dot(U).multiply(U.T)
    W = C + C.T
    return W


def M2(A):
    B, U, _ = DirectionalBreakup(A)
    C = B.dot(U).multiply(U.T) + U.dot(B).multiply(U.T) + U.dot(U).multiply(B)
    W = C + C.T
    return W


def M3(A):
    B, U, _ = DirectionalBreakup(A)
    C = B.dot(B).multiply(U) + B.dot(U).multiply(B) + U.dot(B).multiply(B)
    W = C + C.T
    return W


def M4(A):
    B, _, _ = DirectionalBreakup(A)
    W = B.dot(B).multiply(B)
    return W


def M5(A):
    _, U, _ = DirectionalBreakup(A)
    T1 = U.dot(U).multiply(U)
    T2 = U.T.dot(U).multiply(U)
    T3 = U.dot(U.T).multiply(U)
    C = T1 + T2 + T3
    W = C + C.T
    return W


def M6(A):
    B, U, _ = DirectionalBreakup(A)
    C1 = U.dot(B).multiply(U)
    C1 = C1 + C1.T
    C2 = U.T.dot(U).multiply(B)
    W = C1 + C2
    return W


def M7(A):
    B, U, _ = DirectionalBreakup(A)
    C1 = U.T.dot(B).multiply(U.T)
    C1 = C1 + C1.T
    C2 = U.dot(U.T).multiply(B)
    W = C1 + C2
    return W


def M8(A):
    _, U, G = DirectionalBreakup(A)
    W = np.zeros_like(G)
    N = G.shape[0]
    for i in range(N):
        J = np.where(U[i, :])[1]
        for j1 in range(len(J)):
            for j2 in range(j1+1, len(J)):
                k1 = J[j1]
                k2 = J[j2]
                if A[k1, k2] == 0 and A[k2, k1] == 0:
                    W[i, k1] += 1
                    W[i, k2] += 1
                    W[k1, k2] += 1
    W = csr_matrix(W + W.T)
    return W


def M9(A):
    _, U, G = DirectionalBreakup(A)
    W = np.zeros_like(G)
    N = G.shape[0]
    for i in range(N):
        J1 = np.where(U[i, :])[1]
        J2 = np.where(U[:, i])[0]
        for j1 in range(len(J1)):
            for j2 in range(len(J2)):
                k1 = J1[j1]
                k2 = J2[j2]
                if A[k1, k2] == 0 and A[k2, k1] == 0:
                    W[i, k1] += 1
                    W[i, k2] += 1
                    W[k1, k2] += 1
    W = csr_matrix(W + W.T)
    return W


def M10(A):
    return M8(A.T)


def M11(A):
    B, U, G = DirectionalBreakup(A)
    W = np.zeros_like(G)
    N = G.shape[0]
    for i in range(N):
        J1 = np.where(B[i, :])[1]
        J2 = np.where(U[i, :])[1]
        for j1 in range(len(J1)):
            for j2 in range(len(J2)):
                k1 = J1[j1]
                k2 = J2[j2]
                if A[k1, k2] == 0 and A[k2, k1] == 0:
                    W[i, k1] += 1
                    W[i, k2] += 1
                    W[k1, k2] += 1
    W = csr_matrix(W + W.T)
    return W


def M12(A):
    return M11(A.T)


def M13(A):
    B, _, G = DirectionalBreakup(A)
    W = np.zeros_like(G)
    N = G.shape[0]
    for i in range(N):
        J = np.where(B[i, :])[1]
        for j1 in range(len(J)):
            for j2 in range(j1+1, len(J)):
                k1 = J[j1]
                k2 = J[j2]
                if A[k1, k2] == 0 and A[k2, k1] == 0:
                    W[i, k1] += 1
                    W[i, k2] += 1
                    W[k1, k2] += 1
    W = csr_matrix(W + W.T)
    return W


def Bifan(A):
    _, U, G = DirectionalBreakup(A)
    NA = np.logical_not(A) & np.logical_not(A.T)
    W = np.zeros_like(G)
    ai, aj = np.where(np.triu(NA, 1))
    for ind in range(len(ai)):
        x = ai[ind]
        y = aj[ind]
        xout = np.where(U[x, :])[1]
        yout = np.where(U[y, :])[1]
        common = np.intersect1d(xout, yout)
        nc = len(common)
        for i in range(nc):
            for j in range(i+1, nc):
                w = common[i]
                v = common[j]
                if NA[w, v]:
                    W[x, y] += 1
                    W[x, w] += 1
                    W[x, v] += 1
                    W[y, w] += 1
                    W[y, v] += 1
                    W[w, v] += 1
    W = csr_matrix(W + W.T)
    return W


# % MOTIFADJACENCY forms the motif adjacency matrix for the adjacency
# % matrix A and the specified motif.
# % 'motif' is one of:
# % M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, M13
# % bifan
# % edge
# % 
# % See http://snap.stanford.edu/higher-order/code.html for
# % the naming conventions.
# %  
# %  W = MotifAdjacency(A, motif) returns
# %    W: the motif adjacency matrix

# % Ignore diagonals and weights
