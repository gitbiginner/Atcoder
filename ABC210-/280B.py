N= int(input())

S = [0]+list(map(int, input().split()))

ans =[0]*(N+1)

for i in range(1,N+1):
    ans[i] = S[i]-sum(ans[0:i])

print(*ans[1:])
    


