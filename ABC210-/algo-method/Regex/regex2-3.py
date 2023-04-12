S = input()

import re
reg = r'^([a-z]+\-)*[a-z]+$'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No")
# https://algo-method.com/tasks/340/editorial
