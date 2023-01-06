from collections import deque
from heapq import heappop, heappush

N, M = map(int, input().split())

# N points
# M loads

edge = [[] for _ in range(N+1)]

for i in range(1, M+1):
    A, B, C = map(int, input().split())
    edge[A].append((B,C))
    edge[B].append((A, C))


INF = 10**10
dist = [INF]*(N+1)
dist[1] = 0

#q = deque()
#q.append(1)

pq = []
heappush(pq, (0,1))
while pq:
    d, now = heappop(pq)
    if dist[now] < d: continue

    for to,c  in edge[now]:
        if dist[to] > dist[now]+c:
            dist[to] = dist[now]+c
            heappush(pq, (dist[to], to))

for  i in range(1, N+1):
    if dist[i] == INF:
        dist[i] = -1
    print(dist[i])
