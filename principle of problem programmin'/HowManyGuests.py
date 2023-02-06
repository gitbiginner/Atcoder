# https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_ai

N, Q = map(int, input().split())

A =list(map(int, input().split()))

L = [None]*Q
R = [None]*Q

for i in range(Q):
    L[i], R[i] = map(int, input().split())

S = [0]*(N+1)

for i in range(N):
    S[i+1] = S[i]+A[i]

ans=0
for i in range(Q):
    ans = S[R[i]]-S[L[i]-1]
    print(ans)
