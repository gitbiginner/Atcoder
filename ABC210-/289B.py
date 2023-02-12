# https://atcoder.jp/contests/abc289/tasks/abc289_b

N, M = map(int,input().split())

A = list(map(int, input().split()))

ans = []
paths = []

for i in range(1, N+1):
    paths.append(i)
    if not i in A:
        ans.extend(reversed(paths))
        paths = []

print(*ans)

