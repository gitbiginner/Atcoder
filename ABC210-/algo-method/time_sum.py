
# https://algo-method.com/tasks/1021/editorial

N = int(input())
A = list(map(int, input().split()))

S = sum(A)
T = sum(map(lambda v: v**2, A))

print((S**2-T)//2)
