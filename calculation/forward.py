def forward(vertices, adj):
    # initialize the dynamic data structure
    A = {v: set() for v in vertices}

    # set to store output triangles
    output = set()

    for s in vertices:
        for t in adj[s]:
            if s < t:
                for v in A[s].intersection(A[t]):
                    # use frozenset to ensure the set of vertices is immutable and hashable
                    output.add(frozenset([v, s, t]))
                A[t].add(s)

    # convert the frozensets back to regular, mutable sets for output
    output = [set(triangle) for triangle in output]
    
    return output

#example
vertices = [1, 2, 3, 4, 5]
adj = {
    1: {2, 3, 4},
    2: {1, 3, 5},
    3: {1, 2},
    4: {1},
    5: {2}
}

forward(vertices, adj)
