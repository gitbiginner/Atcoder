N, Q = map(int, input().split())
A = list(map(int, input().split()))

X = [None]*Q
Y = [None]*Q


for i in range(Q):
    X[i], Y[i] = map(int, input().split())

for i in range(Q):
    print(A[X[i]]) 

