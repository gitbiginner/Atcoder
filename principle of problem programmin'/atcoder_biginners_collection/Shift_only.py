N = int(input())

A = list(map(int, input().split()))

ans = 0


while min(A) > 1:

    for i in range(N):
        if A[i] % 2 == 1:
            print(ans)
            exit()
        else:
            
            A[i] = A[i]/2
    ans += 1


print(ans)



