H, W = map(int, input().split())

S = [None]*(H+1)
S_dot = [None]*(H+1)
T = [None]*(H+1)
T_dot = [None]*(H+1)

for i in range(H):
    S[i] = input()
    S_dot[i] = S[i].count('.')

for i in range(H):
    T[i] = input()
    T_dot[i] = T[i].count('.')


for i in range(H):
    if T_dot[i] == S_dot[i]:
        ans = 'Yes'
    else:
        print('No')
        exit()
    
print(ans)
