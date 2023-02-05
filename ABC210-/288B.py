#https://atcoder.jp/contests/abc288/tasks/abc288_b
N, K = map(int, input().split())

S = [None]*N
for i in range(N):
    S[i] = input()

top_S = S[0:K]
top_S_sorted = sorted(top_S)

for k in range(K):
    print(top_S_sorted[k])
