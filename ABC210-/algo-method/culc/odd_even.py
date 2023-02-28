# https://algo-method.com/tasks/1090

H, W, p, q = map(int, input().split())

if (p+q)%2 == 0:
    print('Black')
else:
    print('White')
    