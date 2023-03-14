#https://algo-method.com/tasks/1101


N  = int(input())
A  = list(map(int, input().split()))

biggest = A[0]

for i in A:

    if biggest >= i:
        print(biggest)
    else:
        print(i)
        biggest = i
