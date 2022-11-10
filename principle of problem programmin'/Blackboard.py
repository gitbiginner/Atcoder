ans = 0
N= int(input())
T = [None]*(N)
A = [None]*(N)
for i in range(N):
    T[i], A[i] = map(str, input().split())
    A[i] = int(A[i])


for i in range(N):
    if T[i] == '+':
        ans += A[i]
        ans = ans%10000
        print(ans)
    elif T[i] == '-':
        ans -= A[i]
        ans = ans%10000
        print(ans)
    elif T[i] == '*':
        ans *= A[i]
        ans = ans%10000
        print(ans)


