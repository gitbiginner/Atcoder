# https://algo-method.com/tasks/1097

N, M = map(int, input().split())


menu = {}

for i in range(N):
    F,C = map(str,input().split())
    C  = int(C)
    menu[F]  = C


X = list( input().split())

ans = 0
for i in X:
    ans += menu[i]

print(ans)
