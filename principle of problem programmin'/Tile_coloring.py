N = int(input())
S = input()

for i in range(0,N-2):
    if S[i] == S[i+1] and S[i] == S[i+2]:
        answer = 'Yes'
        print(answer)
        exit()
    else:
        pass

answer = 'No'

print(answer)

