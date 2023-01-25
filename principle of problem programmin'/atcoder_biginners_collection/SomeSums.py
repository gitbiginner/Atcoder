N, A, B = map(int, input().split())
c = 0
for i in range(1, N+1):
    list_i = list(str(i))
    x = [int(x) for x in list_i]
    if A <= sum(x) <= B:
        c += i
 
print(c)

