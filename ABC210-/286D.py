N, X = map(int,input().split())


AB = [map(int, input().split()) for _ in range(N)]
A,B = [list(i) for i in zip(*AB)]
while X >= 0 and A:
    ma = max(A)
    mp = max(A)*B[A.index(ma)]
    if X < ma:
        B.pop(A.index(ma))
        A.remove(ma)
    elif X < mp :
        B[A.index(ma)]-=1
    elif X>= mp:
        X -= mp

        B.pop(A.index(ma))
        A.remove(ma)
        if X == 0:
            print('Yes')
            exit()
else:
  print('No')
    

