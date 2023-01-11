n, m = map(int, input().split())
edges = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a - 1][b - 1] += c
 
def DFS(now, goal, flow=10**10):
    come[now] = True
    if now == goal:
        return flow
    for to in range(n):
        if edges[now][to] <= 0 or come[to]: continue
        f = DFS(to, goal, min(flow, edges[now][to]))
 
        if f <= 0: continue
        edges[now][to] -= f
        edges[to][now] += f
        return f
    return 0
 
ans = 0
while True:
    come = [False] * n
    flow = DFS(0, n - 1)
    if flow <= 0:
        break
    ans += flow
 
print(ans)
