N = int(input())

A = list(map(int, input().split()))

# 入力
Q = int(input()) # クエリ数

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        k, x = query[1:]
        k -= 1
        A[k] = x
    if  query[0] == 2:
        k = query[1]
        k -= 1
        print(A[k])
