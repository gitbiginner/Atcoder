N, M= map(int, input().split())
A = [None]*N
B = [None]*N
ans = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    ans[a].append(str(b))
    ans[b].append(str(a))


for i in range(1, N+1):
    ans2 = '{'+','.join(ans[i])+'}'
    print(i,':',ans2)

