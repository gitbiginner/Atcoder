import re 
S = input()
reg =r'\d{3}'

if re.search(reg, S):
    print("Yes")
else:
    print("No")
# https://algo-method.com/tasks/294

# https://algo-method.com/descriptions/80
