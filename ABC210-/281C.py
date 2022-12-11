N, T = map(int, input().split())
A = list(map(int, input().split()))

sum_A = sum(A)

T = T % sum_A
for i, a in enumerate(A):
    if a > T:
        print(i+1, T)
        break
    else:
        T = T-a

