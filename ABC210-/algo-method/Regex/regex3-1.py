# https://algo-method.com/tasks/293
S = input()

import re
reg = r'\d'

if re.search(reg, S):
    print("Yes")
else:
    print("No")
