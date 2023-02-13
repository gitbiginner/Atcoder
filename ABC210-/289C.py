# https://atcoder.jp/contests/abc289/tasks/abc289_c

n, m = map(int, input().split())
a = [None for _ in range(m)]
for i in range(m):
    c = int(input())
    a[i] = set(map(int, input().split()))
range_st = set(range(1, n + 1))
cnt = 0
for i in range(2**m):
    st = set()
    for j in range(m):
        # print(i >> j & 1 == 1, end=", ")
        if i >> j & 1 == 1:
            st |= a[j]
    if st == range_st:
        cnt += 1
print(cnt)


