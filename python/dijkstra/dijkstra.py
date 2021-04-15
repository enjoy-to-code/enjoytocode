import numpy as np
from scipy.sparse.csgraph import shortest_path

M = np.array([[ 0, 6,  7,  0,  0, 15],
              [ 6, 0,  9,  18, 0, 0],
              [ 7, 9,  0,  12, 0, 3],
              [ 0, 18, 12, 0,  8, 0],
              [ 0, 0,  0,  8,  0, 9],
              [15, 0,  3,  0,  9, 0]])

D, Pr = shortest_path(M, directed=False, method='D', return_predecessors=True)

def get_path(Pr, i, j):
    path = [j]
    k = j
    while Pr[i, k] != -9999:
        path.append(Pr[i, k])
        k = Pr[i, k]
    return path[::-1]

print("shortest path    [0..4]: ", get_path(Pr,0,4))
print("length           [0..4]: ", D[0,4])
print("")
print("shortest path    [0..5]: ", get_path(Pr,0,5))
print("length           [0..5]: ", D[0,5])


