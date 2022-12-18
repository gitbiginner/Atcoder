n, m = map(int, input().split())

S = list(input() for _ in range(n))
ans = 0
#print(type(S))

for i in range(n):
    for j in range(i+1, n):
        flg = True
        for k in range(m):
            a = S[i][k]
            b = S[j][k]
            if a == 'x' and b == 'x':
                flg = False
            else:
                pass
            
        if flg == True:
            ans += 1

print(ans)

