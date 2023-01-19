#https://atcoder.jp/contests/abc278/tasks/abc278_d


from collections import defaultdict
 
# input
n = int(input())
a = list(map(int, input().split()))
q = int(input())
queries = [ list(map(int, input().split())) for i in range(q) ]
 
# processing
d = defaultdict(int)
for i in range(n):
	d[i] = a[i]
for v in queries:
	if v[0] == 1:
		d = defaultdict(lambda x=v[1]: x)
	if v[0] == 2:
		d[v[1] - 1] += v[2]
	if v[0] == 3:
		print(d[v[1] - 1])
