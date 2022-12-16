N, Q = map(int, input().split())

A = [i+1 for i in range(N)]
flip = False
ans  =[]
for i in range(Q):
    Query = list(map(int, input().split()))
    if Query[0] == 1:
        [i, x, y]  = Query
        x -= 1
        if flip:
            x = N-1-x
        A[x] = y
    if Query[0] == 2:
        flip = not flip
    if Query[0] == 3:
        [i,x] = Query
        x-=1
        if flip:
            x = N-1-x
        ans.append(A[x])

for i in range(len(ans)):
    print(ans[i])
