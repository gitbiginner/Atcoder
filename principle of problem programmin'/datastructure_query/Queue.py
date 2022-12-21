from collections import deque

Q = int(input())

Queries = [input().split() for  i  in range(Q)]


S  = deque()

for i in range(Q):
    if Queries[i][0] == '1':
        S.append(Queries[i][1:])
    if Queries[i][0] == '2':
        print(''.join(S[0]))
    if Queries[i][0] == '3':
        S.popleft()
