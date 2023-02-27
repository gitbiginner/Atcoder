# https://algo-method.com/tasks/1089

N = int(input())

for i  in range(1, N+1):
    if i % 12 == 0:
        print('FizzBuzz')
    elif i % 6 == 0:
        print('Buzz')
    elif i % 4 == 0:
        print('Fizz')
    else:
        print(i)
