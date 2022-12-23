N = int(input())
Sg = []

ans='Yes'
for i in range(N):
    S = input()

    if S[0] in 'HDCS' and S[1] in 'A23456789TJQK':
        if S in Sg:
            ans='No'
        else:
            Sg.append(S)
    else:
        ans='No'

print(ans)

