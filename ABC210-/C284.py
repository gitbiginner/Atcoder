from sys import setrecursionlimit

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

setrecursionlimit(10**7)
N, M = map(int, input().split())
if N * M == 0:
    print(max(N,M))
    exit()
else:
    edge = np.array([input().split() for _ in range(M)], dtype = np.int64).T


    tmp = np.ones(M, dtype = np.int64).T
    graph = csr_matrix((tmp, (edge[:] -1)), (N, N))



    n, labels = connected_components(graph)
    print(n)
