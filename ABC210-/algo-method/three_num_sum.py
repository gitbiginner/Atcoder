
# https://algo-method.com/tasks/1024/editorial

ans = 0
for x in range(1, N + 1):
    for y in range(1, N + 1):
        for z in range(1, N + 1):
            if x + y + z <= M:
                ans += 1
#rrr
