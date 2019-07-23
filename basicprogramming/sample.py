def reachable(A, x, y):
    M = []
    W = [x]
    while W != []:
       u = W.pop()
       if u == y:
            return True
       M.append(u)
       for v in A[u]:
           if not v in M:
               W.append(v)
    return False

A = { 1: [2,5], 2: [1,6], 3: [2],
      4: [5],   5: [2,6], 6: [3] }
print(reachable(A, 1, 6))  # True
print(reachable(A, 1, 4))  # False

