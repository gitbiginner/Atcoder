#https://atcoder.jp/contests/abc285/tasks/abc285_a

a,b = map(int, input().split())

if (2*a == b) or(2*a+1 == b):
    print('Yes')
else:
    print('No') 
