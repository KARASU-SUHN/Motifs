import numpy as np

def RandIndex(c1, c2):
    if len(c1.shape) > 1 or len(c2.shape) > 1:
        raise ValueError('RandIndex: Requires two vector arguments')

    C = Contingency(c1, c2)  # form contingency matrix

    n = np.sum(np.sum(C))
    nis = np.sum(np.sum(C, axis=1) ** 2)  # sum of squares of sums of rows
    njs = np.sum(np.sum(C, axis=0) ** 2)  # sum of squares of sums of columns

    t1 = n * (n - 1) / 2  # total number of pairs of entities
    t2 = np.sum(np.sum(C ** 2))  # sum over rows & columns of nij^2
    t3 = 0.5 * (nis + njs)

    # Expected index (for adjustment)
    nc = (n * (n ** 2 + 1) - (n + 1) * nis - (n + 1) * njs + 2 * nis * njs / n) / (2 * (n - 1))

    A = t1 + t2 - t3  # no. agreements
    D = -t2 + t3  # no. disagreements

    TP = 0.5 * np.sum(C ** 2 - C)
    FP = 0.5 * (njs - n) - TP
    FN = 0.5 * (nis - n) - TP
    P = TP / (TP + FP)
    R = TP / (TP + FN)
    F1 = 2 * P * R / (P + R)

    if t1 == nc:
        AR = 0  # avoid division by zero; if k=1, define Rand = 0
    else:
        AR = (A - nc) / (t1 - nc)  # adjusted Rand - Hubert & Arabie 1985

    RI = A / t1  # Rand 1971 - Probability of agreement
    MI = D / t1  # Mirkin 1970 - p(disagreement)
    HI = (A - D) / t1  # Hubert 1977 - p(agree)-p(disagree)

    return AR, F1, RI, MI, HI


def Contingency(Mem1, Mem2):
    if len(Mem1.shape) > 1 or len(Mem2.shape) > 1:
        raise ValueError('Contingency: Requires two vector arguments')

    Cont = np.zeros((np.max(Mem1), np.max(Mem2)))

    for i in range(len(Mem1)):
        Cont[Mem1[i] - 1, Mem2[i] - 1] += 1

    return Cont


# %RANDINDEX - calculates Rand Indices to compare two partitions
# % ARI=RANDINDEX(c1,c2), where c1,c2 are vectors listing the 
# % class membership, returns the "Hubert & Arabie adjusted Rand index".
# % [AR,RI,MI,HI]=RANDINDEX(c1,c2) returns the adjusted Rand index, 
# % the unadjusted Rand index, "Mirkin's" index and "Hubert's" index.
# %
# % See L. Hubert and P. Arabie (1985) "Comparing Partitions" Journal of 
# % Classification 2:193-218

# %(C) David Corney (2000)   		D.Corney@cs.ucl.ac.uk
# % Tao Wu added the implementation for F1 (Jan/20/2016)
