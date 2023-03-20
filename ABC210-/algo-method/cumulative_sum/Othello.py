# https://algo-method.com/tasks/1104


def run_length(S):
    i = 0
    prev = S[0]
    res = []
    for c in S:
        if prev == c:
            i += 1
        else:
            res.append(i)
            i = 1
            prev  =  c

    res.append(i)
    return res


N = int(input())
S = str(input())

A = run_length(S)

count = 0
while len(A)>=2:
    x = A.pop()
    count += x
    A[-1] += x+1

print(count)
