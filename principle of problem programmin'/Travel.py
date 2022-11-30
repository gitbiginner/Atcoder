N, K = map(int, input().split())

if K >= (2*N-2):
    if K % 2 == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')
