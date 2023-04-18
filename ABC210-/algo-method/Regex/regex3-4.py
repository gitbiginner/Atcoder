#https://algo-method.com/tasks/296

import re
S = input()

reg = r'\w+@\w+\.\w{1,4}$'

if re.search(reg, S):
    print("Yes")
else:
    print("No")



