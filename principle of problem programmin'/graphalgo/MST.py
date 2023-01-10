import sys
sys.setrecursionlimit(10**6)
 
N, M = map(int, input().split())
 
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
 
edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()

ans = 0
for c, a, b in edges:
    if same(a, b):
        continue
    unite(a, b)
    ans += c
print(ans)

        
    
 

