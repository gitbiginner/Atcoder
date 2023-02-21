# https://algo-method.com/tasks/1026

N = int(input())
A = list(map(int, input().split()))
Q = int(input())


S = [0]+[None]*(N+1)

for i in range(N):
    S[i+1] = S[i]+A[i]


for i in range(Q):
    l,r = map(int, input().split())
    print(S[r]-S[l])
