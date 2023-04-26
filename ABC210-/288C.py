
N,M=map(int,input().split())
from collections import *
edge=[[] for _ in range(N)]
 
for i in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    edge[a].append(b)
    edge[b].append(a)
P=[-1]*N
c=0
for i in range(N):
    if P[i]!=-1:
        continue
    c+=1
    S=deque([i])
    while len(S)>0:
        cp=S.popleft()
        for ii in edge[cp]:
            if P[ii]==-1:
                S.append(ii)
                P[ii]=c
 
print(M-N+c)
