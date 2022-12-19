N, C =  input().split()

A = input()

ans = 0

for i in range(int(N)):
    if A[i] == "W":
        ans += 0
    if A[i] == "B":
        ans += 1
    if A[i] == "R":
        ans += 2

if ans %3 == 0 and C =='W':
    print('Yes')
elif ans %3 == 1 and C =='B':
    print('Yes')
elif ans %3 == 2 and C =='R':
    print('Yes')
else:
    print('No')
