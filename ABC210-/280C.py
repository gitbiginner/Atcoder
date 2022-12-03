S = str(input())
T = str(input())

S = S+'A'
for i in range(len(S)):
    if S[i] == T[i]:
        pass
    elif S[i] != T[i]:
        print(i+1)
        exit()



