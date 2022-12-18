N = int(input())
S = list(str(input()))

count_quo = 0
change = True


for i in range(N):
    if S[i] == '"':
        count_quo += 1
        if count_quo %2 == 0:
            change = True
        else:
            change=False
    elif S[i] ==",":
        if count_quo %2 == 0 and change==True:
            S[i] = S[i].replace(',', '.')
#print(S) 
#print(type(S))
#print(count_quo)       
#print(change)
#print(s)   
ans = "".join(S)
print(ans)
