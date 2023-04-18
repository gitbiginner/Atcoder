# https://algo-method.com/tasks/295
import re
S = input()

reg = r'\d{3}-\d{4}'
if re.search(reg, S):
    print("Yes")
else:
    print("No")

