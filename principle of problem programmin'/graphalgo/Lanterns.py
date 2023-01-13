from collections import deque

N,M   = map(int, input().split())

A = list(map(int, input().split()))

S = 0

for i in range(N):
    S += A[i]*(2**i)

B = [0]*M

for i in range(M):
    X, Y, Z = map(int, input().split())
    B[i] = 2**(X-1)+2**(Y-1)+2**(Z-1)

v = [-1]*(2**N+1)
q = deque()

q.append(S)
v[S] = 0

while len(q) != 0:
    k = q[0]
    q.popleft()
    for i in range(M):
        t = k^B[i]
        if v[t] != -1:
            continue
        v[t] = v[k]+1
        q.append(t)

print(v[2**N-1])




