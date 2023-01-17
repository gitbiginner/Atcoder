#https://atcoder.jp/contests/abc278/tasks/abc278_b


H, M = map(int, input().split())

A = H//10
B = H-10*A
C = M//10
D = M-10*C

if (0<=10*A+C<=23) and (0<=10*B+D<=59):
    print(H, M)
elif  H == 23:
    print(0, 0)

elif 10*A+C>=24:
    print(H+1,0)

elif (10*B+D>=60) and H<10:
    print(10,0)

elif (10*B+D>=60) and H<20:
    print(20,0)

else:
    print(H+1, 0)

