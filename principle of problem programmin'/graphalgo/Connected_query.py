import sys
sys.setrecursionlimit(10**6)
 
N, Q = map(int, input().split())
 
parent = [-1] * (N+1)
 
def root(x):
    if parent[x] < 0:
        return x
    parent[x] = root(parent[x])
    return parent[x]
 
def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    parent[x] += parent[y]
    parent[y] = x
 
def same(x, y):
    return root(x) == root(y)
 
 
for _ in range(Q):
    q, u, v = list(map(int, input().split()))
    if q == 1:
        unite(u, v)
    else:
        if same(u, v):
            print("Yes")
        else:
            print("No")
        
    
 

