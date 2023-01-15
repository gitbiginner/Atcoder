# https://atcoder.jp/contests/abc285/tasks/abc285_c

S = input()

S = [s for s in S]

answer = 0
for i in range(len(S)):
    answer = answer*26+ord(S[i])-64

print(answer)
