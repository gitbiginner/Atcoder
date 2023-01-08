n = int(input())
a0 = list(map(int,input().split()))
a = [m-1 for m in a0]
a.reverse()

dp = [0]*n
for i in range(n-1):
    dp[a[i]] += 1 + dp[n-i-1]
for i in range(n):
    print(dp[i],end=" ")

