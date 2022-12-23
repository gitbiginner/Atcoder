
n = int(input())
dsu = dict()
 
def find_set(a):
    if a not in dsu:
        dsu[a] = a
    elif dsu[a] != a:
        dsu[a] = find_set(dsu[a])
    return dsu[a]
 
def union_sets(a, b):
    dsu[a] = dsu[b] = max(a, b)
 
for i in range(n):
    a, b = map(int, input().split())
    union_sets(find_set(a), find_set(b))
 
print(find_set(1))
