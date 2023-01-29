#https://atcoder.jp/contests/abs/tasks/abc085_b
  
N = int(input())

d = [None]*N
for i in range(N):
  d[i] = int(input())
  
print(len(set(d)))
