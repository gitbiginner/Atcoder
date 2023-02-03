# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_d

N =int(input())

n=N
ans = [0]*10

i = 9
while n > 0:
    ans[i] = n%2
    n = n//2
    i = i-1
for i in range(10):
    print(ans[i], end='')

