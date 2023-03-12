# https://algo-method.com/tasks/1099

A, B, C = map(int, input().split())
Y, M, D, X = map(int, input().split())

Y1, M1, D1 = map(int, input().split())

def day(a, b, c, y, m, d):
    return (y-1)*a*b+(m-1)*b+d-1

t0 = day(A, B, C, Y, M, D)
#print((X-1)*t0%C)

t1 = day(A, B, C, Y1, M1, D1)
X -= 1

ans = (X + (t1 - t0) % C) %C
ans +=1
print(ans)
