N, L = map(int, input().split())

A = [None]*N
B = [None]*N

for i in range(N):
    A[i], B[i] = input().split()
    A[i] = int(A[i])

Answer = 0

for i in range(N):
    if B[i] == 'E':
        Answer = max(Answer, L-A[i])
    if B[i] == 'W':
        Answer = max(Answer, A[i])

print(Answer)
