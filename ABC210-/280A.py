H, W = map(int, input().split())

S = [None]*(H)
ans = 0 
for i in range(H):
    S[i] = input()
    dot_cnt = S[i].count('#')
    ans += dot_cnt
    
print(ans)


