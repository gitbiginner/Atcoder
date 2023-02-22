#https://algo-method.com/tasks/1027

N = int(input())
d = list(map(int, input().split()))
Q = int(input())

S = [0]+[None]*(N+1)

for i in range(N-1):
    S[i+1] = S[i]+d[i]


for _ in range(Q):
    l, r = map(int, input().split())
    print(S[r]-S[l])


