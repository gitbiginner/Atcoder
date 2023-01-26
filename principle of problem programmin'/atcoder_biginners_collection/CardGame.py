# https://atcoder.jp/contests/abs/tasks/abc088_b
N = int(input())

A = list(map(int, input().split()))

A.sort(reverse=True)

Alice = []
Bob = []

for i in range(N):
    if i % 2 == 0:
        Alice.append(A[i])
    else:
        Bob.append(A[i])

sum_A = sum(Alice)
sum_B = sum(Bob)

print(sum_A-sum_B)

