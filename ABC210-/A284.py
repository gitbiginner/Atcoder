N= int(input())

S = [None]*N
for i in range(1,N+1):
    S[-i] = input()

for i in range(N):
    print(S[i])

