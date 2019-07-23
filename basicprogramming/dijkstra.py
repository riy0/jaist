def find_min(W, D):
    u = W[0]
    for v in W:
        if D[u] > D[v]:
            u = v
    return u
    
def dijkstra(A, c, x, y):
    D = {x: 0}
    W = [x]
    P = {}
    while W != []:
       u = find_min(W, D)
       W.remove(u)
       if u == y:
            break
       for v in A[u]:
           dv = D[u] + c(u, v)
           if not v in D or dv < D[v]:
               D[v] = dv
               P[v] = u
               W.append(v)
    if y in D:
        return D[y]
    else:
        return None

A = { 1: [2,5], 2: [1,6], 3: [2],
      4: [5],   5: [2,6], 6: [3] }
C = { (1,2): 9, (1,5): 3, (2,1): 9, (2,6): 2,
      (3,2): 1, (4,5): 1, (5,2): 4, (5,6): 8,
      (6,3): 1 }

print(dijkstra(A, lambda x,y: C[(x,y)], 1, 6))
# 9
print(dijkstra(A, lambda x,y: C[(x,y)], 1, 4))
# None
