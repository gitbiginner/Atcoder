from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

count = defaultdict((int))
for i in range(N):
    count[A[i]] += 1

count_list = list(count.values())

from math import factorial
def nCr(n, r):
    nume = factorial(n)
    denomi = factorial(n-r)*factorial(r)
    return  nume//denomi


ans=0
for i in range(len(count_list)):
    if count_list[i] >= 3:
        ans += nCr(count_list[i], 3)
        

print(ans)
