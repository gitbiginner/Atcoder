from math import factorial

n, r = map(int, input().split())

def nCr(n, r):
    n_fact = factorial(n)
    n_r = n-r
    denomi = factorial(r)*factorial(n_r)
    ans = n_fact//denomi
    return ans

mod = 1000000007
answer = nCr(n,r) 
print(answer%mod)
