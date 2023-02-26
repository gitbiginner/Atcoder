# https://algo-method.com/tasks/1029/editorial


N= int(input())
L = list(map(int, input().split()))


count = [0]*(10**5+1) # 10**5

for i in L:
    count[i] += 1 

acc = [0]*(10**5+2) # 10**5 +1


for ind, cnt in enumerate(count):
    acc[ind+1] = acc[ind]+cnt


Q = int(input())


for _ in range(Q):
    A, B = map(int, input().split())
    print(acc[B+1]-acc[A])


