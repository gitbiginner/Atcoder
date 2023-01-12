n = int(input())

N = 2*n+2
S = 2*n
G = 2*n+1
edge = [[0] * (N) for _ in range(N)]

C = [input() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if C[i][j] == '#':
            edge[i][n+j] = 1
 
for i in range(n):
    edge[S][i] = 1
    edge[n+i][G] = 1
 
come = [False] * (N)
 
def dfs(now, goal, flow):    
    come[now] = True
    if now == goal:
        return flow
    for to in range(0, N):
        if edge[now][to] == 0 or come[to]:
            continue
        f = dfs(to, goal, min(flow, edge[now][to]))
        if f == 0:
            continue
        edge[now][to] -= f
        edge[to][now] += f
        return f
    return 0
    
 
ans = 0
while True:
    come = [False] * (N+1)
    f = dfs(S, G, 10**10)
    if f == 0:
        break
    ans += f
 
print(ans)




