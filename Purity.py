import numpy as np

def Purity(labels, clusters):
    assert len(labels) == len(clusters)
    overlap = 0
    u_clusters = np.unique(clusters)
    
    for i in range(len(u_clusters)):
        k = u_clusters[i]
        # Find best cluster for this label
        assignments = labels[clusters == k]
        overlap += np.sum(assignments == np.argmax(np.bincount(assignments)))
    
    score = overlap / len(labels)
    return score


# %PURITY - calculates purity to evaluate clustering
# % score=Purity(labels, clusters)  where labels assigns the
# % ground truth and clusters is the clustering assignment.
