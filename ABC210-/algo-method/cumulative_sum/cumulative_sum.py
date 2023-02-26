# https://algo-method.com/tasks/1025

N =int(input())
A = list(map(int, input().split()))

Q = int(input())



S = [0]+[None]*(N+1)
for i in range(N):
    S[i+1] = S[i]+A[i]

for i in range(Q):
    q = int(input())
    print(S[q])



