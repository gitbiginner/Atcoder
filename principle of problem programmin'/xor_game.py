N = int(input())
A = list(map(int, input().split()))

XOR = A[0]
for i in range(1, N):
    XOR = (XOR ^ A[i])

if XOR >= 1:
    print('First')
else:
    print('Second')
