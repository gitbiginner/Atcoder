A, B = map(int, input().split())

ans = 10**18+1

time  = 0
g = 1

for i in range(10**9+1):
    reach_time = B*i + A /(g)**0.5
    if reach_time < ans:
        ans = reach_time
        g+=1
    else:
        print('{:.10f}'.format((ans)))
        exit()

