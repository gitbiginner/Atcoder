# https://algo-method.com/tasks/1028

N, D = map(int, input().split())
X = list(map(int, input().split()))

ans = 0

S = [0]+[None]*(N+1)

for i in range(N):
    S[i+1] = S[i]+X[i]


for i in range(N-D+1):
    sum_cus = S[i+D]-S[i]
    if sum_cus >= ans:
        ans = sum_cus
        answeri, period = i, i+D-1

print(str(answeri)+'~'+str(period))


