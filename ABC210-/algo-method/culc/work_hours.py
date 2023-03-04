# 
# https://algo-method.com/tasks/1093

ans = 0
for i in range(30):
    H1, M1, H2, M2 = map(int, input().split())
    minuite = 60*(H2-H1)+M2-M1
    if H1==M1==H2==M2==0:
        continue;
    elif 360 < minuite <= 480:
        minuite= minuite-45
    elif minuite > 480:
        minuite= minuite-60 

    ans += minuite

print(ans//60, ans%60)
