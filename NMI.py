import numpy as np

def NMI(classes, clusters):
    assert len(classes) == len(clusters)

    uw = np.unique(classes)
    uc = np.unique(clusters)

    Cw = counts(classes, uw)
    Cc = counts(clusters, uc)

    I = 0
    N = len(classes)

    for k in range(len(uw)):
        for j in range(len(uc)):
            common = np.intersect1d(np.where(classes == uw[k])[0], np.where(clusters == uc[j])[0])
            nc = len(common)
            if nc == 0:
                continue
            I = I + (nc / N) * np.log(N * nc / (Cw[k] * Cc[j]))

    z = 2 * I / (entropy(classes) + entropy(clusters))
    return z


def counts(x, ux):
    N = len(ux)
    C = np.zeros(N)
    for i in range(len(ux)):
        C[i] = np.sum(x == ux[i])
    return C


def entropy(x):
    ux = np.unique(x)
    H = 0
    N = len(x)
    for i in range(len(ux)):
        nuxi = np.sum(x == ux[i])
        H = H - (nuxi / N) * np.log(nuxi / N)
    return H


# %NMI - calculates normalized mutual information to evaluate clustering
# % z = NMI(classes, clusters) where classes are the true classes
# % and clusters is the clustering assignment.
