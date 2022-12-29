from sys import stdin; input = stdin.readline
 
SEGLEN = 1<<18
INF = 0
tree = [INF]*(SEGLEN * 2)
 
def update(i, x): # i: 0-indexed
	i += SEGLEN
	tree[i] = x
	while True:
		i //= 2
		if i == 0: break
		tree[i] = max(tree[i*2], tree[i*2+1])
 
def get_max(l, r): #l, r: 0-indexed
	result = INF
	l += SEGLEN
	r += SEGLEN
	while l < r:
		if l & 1:
			result = max(result, tree[l])
			l += 1
		l >>= 1
		if r & 1:
			result = max(result, tree[r - 1])
			#r -= 1
		r >>= 1
	return result
 
N, Q = map(int, input().split())
 
for i in range(Q):
	t, a, b = map(int, input().split())
	if t==1: update(a-1, b)
	if t==2: print(get_max(a-1, b-1))
