#https://atcoder.jp/contests/abc278/tasks/abc278_c

N, Q =map(int, input().split())

S  = set()

#print(type(S))

for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        S.add((A, B))
        #print(S)
    if T== 2:
        S.discard((A, B))
        #print(S)
    if T == 3:
        if (A, B) in S and (B, A) in S:
            print("Yes")
        else:
            print("No")


