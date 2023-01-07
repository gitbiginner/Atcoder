T = int(input())

test = [[] for _ in range(T)]


for i in range(T):
    ans=0
    N = int(input())
    test[i] = list(map(int, input().split()))
    for j in range(N):
        if test[i][j] %2 == 1:
            ans+=1
    print(ans)



