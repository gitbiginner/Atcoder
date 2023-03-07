# https://algo-method.com/tasks/1098

N, M = map(int,input().split())
ans = N


while N:
    if N-M < 0:
        print(ans)
        exit()
    else:
        N = N-M+1
        ans+=1
