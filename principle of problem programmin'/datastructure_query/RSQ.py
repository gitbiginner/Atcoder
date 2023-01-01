N, Q = map(int, input().split())

seg = [0]*(1<<19)

def add(pos, x):
	pos += (1<<18)
	seg[pos] = x
	pos = pos//2
	while pos:
		seg[pos] = seg[pos*2] + seg[pos*2+1]
		pos//= 2

def get_sum(l, r):
	l = l+(1<<18)
	r = r+(1<<18)
	ans = 0
	while l<r:
		if l % 2 == 1:
			ans = ans + seg[l]
			l+=1
		if r % 2 == 1:
			ans = ans + seg[r-1]
			r-=1
		l = l//2
		r = r//2
	return ans

for _ in range(Q):
	query = input().split()
	if query[0] =='1':
		pos, x  = int(query[1]), int(query[2])
		add(pos, x)
	if query[0] == '2':
		l, r = int(query[1]), int(query[2])
		print(get_sum(l, r))


