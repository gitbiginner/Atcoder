D = int(input())
N = int(input())

L = [None]*N
R = [None]*N

for i in range(N):
    L[i], R[i] = map(int, input().split())

ans = [0]*(D+2)

for i in range(N):
    ans[L[i]] += 1
    ans[R[i]+1] -= 1

Answer = [0]+[None]*(D+1)

for d in range(1, D+1):
    Answer[d] = Answer[d-1]+ans[d]

for d in range(1, D+1):
    print(Answer[d])

