N, P, Q, R, S  = map(int, input().split())
A = [0] + list(map(int, input().split()))

list = A
list[P:Q+1], list[R:S+1] = list[R:S+1], list[P:Q+1]


print(*list[1:])
#https://atcoder.jp/contests/abc286/tasks/abc286_a
