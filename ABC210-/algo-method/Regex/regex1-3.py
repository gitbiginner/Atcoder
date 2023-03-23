# https://algo-method.com/tasks/299

S = input()

if 1 <= len(S) <= 100:
    if 'a' in S[0:5] and S.count('b')== 10:
        print('Yes')
    else:
        print('No')
    
else:
    print('No')
