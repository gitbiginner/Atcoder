N, T = map(int, input().split())

C = list(map(int, input().split()))
R = list(map(int, input().split()))

r = 0
ans = 0
for i in range(N):
    if C[i] == T and r <R[i]:
        #ans = R[i]
        r = R[i]
        ans = i+1


if ans == 0:
    for i in range(N):
        if C[i] == C[0] and r <R[i]:
            #ans = R[i]
            r = R[i]
            ans = i+1
print(ans)
