# https://atcoder.jp/contests/abs/tasks/arc089_a


N = int(input())
X = []
x,y,t = 0,0,0
for i in range(N):
    X.append(list(map(int, input().split())))
possibility = True
for j in range(N):
    if X[j][0] % 2 == (X[j][1] + X[j][2]) % 2:
        if X[j][0] - t < abs(X[j][1] - x) + abs(X[j][2] - y):
            possibility = False
        t = X[j][0]
        x = X[j][1]
        y = X[j][2]
    else:
        possibility = False
        break
    
if possibility:
    print('Yes')
else:
    print('No')
