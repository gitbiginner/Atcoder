from collections import deque

N, M = map(int, input().split())

edge = [[] for _ in range(N+1)]

for i in range(1, M+1):
    A, B= map(int, input().split())
    edge[A].append(B)
    edge[B].append(A)

INF = -1
dist = [INF]*(N+1)
dist[1] =  0

q = deque()
q.append(1)

while q:
    now = q.popleft()
    for to in edge[now]:
        if dist[to] != INF: continue
        dist[to] = dist[now]+1
        q.append(to)

for i in range(1, N+1):
    print(dist[i])

