# https://algo-method.com/tasks/1102


N  = int(input())
A  = list(map(int, input().split()))


from collections import defaultdict
biggest = A[0]
count = defaultdict(int)
for i in range(N):
    count[A[i]] += 1

    if biggest >= A[i]:
        print(count[biggest])
    else:
        biggest = A[i]
        print(count[biggest])
    