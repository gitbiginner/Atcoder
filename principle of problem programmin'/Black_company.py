D, N = map(int, input().split())

L = [None]*N
R = [None]*N
H = [None]*N

for i in range(N):
    L[i], R[i], H[i] = map(int, input().split())

LIM = [24]*(D+1)

for i in range(N):
    for j in range(L[i],R[i]):
        LIM[j]  = min(LIM[j], H[i])

Answer = 0
for i in range(1, D+1):
    Answer += LIM[i]

print(Answer)

