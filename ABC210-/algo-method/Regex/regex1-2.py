# https://algo-method.com/tasks/298

S = input()

o_count = S.count('o')


if 1 <= o_count <= 100:
    if S[-1] == "d" and S[0:4] == "meth":
        print('Yes')
    else:
        print('No')
else:
    print('No')
