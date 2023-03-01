# https://algo-method.com/tasks/1091


N =int(input())

if N % 400 == 0:
    print('Yes')
elif N % 100 == 0:
    print('No')
elif N % 4 == 0:
    print('Yes')
else:
    print('No')
