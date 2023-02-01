#https://atcoder.jp/contests/abs/tasks/arc065_a

S = input()

SS = S.replace("erace","").replace("eracer","").replace("dream","").replace("dreamer","")

if SS == "":
  print("Yes")
else:
  print("No")
