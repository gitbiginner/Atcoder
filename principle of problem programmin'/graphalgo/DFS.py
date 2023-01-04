from sys import setrecursionlimit
setrecursionlimit(10**7)

N, M = map(int, input().split())

edge= [[] for _ in range(N+1)]

for i in range(1, M+1):
    A, B = map(int, input().split())
    edge[A].append(B)
    edge[B].append(A)

come = [None]*(N+1)

def dfs(x):
    come[x] = True
    for to in edge[x]:
        if come[to] == True:
            continue
        dfs(to)

dfs(1)

if all(come[1:]):
    print('The graph is connected.')       
else:
    print('The graph is not connected.')
