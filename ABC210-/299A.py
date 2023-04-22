import re
N =int(input())

S = input()

reg = r"\|\W*\*\W*\|"

if re.search(reg, S):
    print("in")
else:
    print("out")
