N = int(input())


A = []
for i in range(N):
    L, R = map(int, input().split())
    A.append([R,L])

A.sort()

CurrentTime = 0
Answer = 0

for i in range(N):
    if CurrentTime <= A[i][1]:
        CurrentTime = A[i][0]
        Answer+=1

print(Answer)

