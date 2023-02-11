#https://atcoder.jp/contests/abc289/tasks/abc289_a
s = input()

s_rep = s.replace("0","A").replace("1","B")
print(s_rep.replace("A","1").replace("B", "0"))
