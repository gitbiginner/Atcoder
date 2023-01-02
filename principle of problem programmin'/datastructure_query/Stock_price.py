from collections import deque
N = int(input())
q = deque()

A = list(map(int, input().split()))
ans = []

for i in range(N):
    while q and q[-1][0] <= A[i]:
        q.pop()
    if q:
        ans.append(q[-1][1])
    else:
        ans.append(-1)
    q.append([A[i], i+1])

print(*ans)

