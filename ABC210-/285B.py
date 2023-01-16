# https://atcoder.jp/contests/abc285/tasks/abc285_b
n = int(input())
s = input()
 
for i in range(1, n):
  for k in range(n-i):
    if s[k] == s[k+i]:
      print(k)
      break
  else:
    print(n-i)


