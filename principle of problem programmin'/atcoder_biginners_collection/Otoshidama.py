# https://atcoder.jp/contests/abs/tasks/abc085_c

N, Y=map(int, input().split())
 
 
for i in range(N+1):
	for j in range(0,N+1-i):
		if 1000*i + 5000*j +10000*(N-i-j) == Y:
         
			print(N-i-j,j,i)
			exit()
else:
	print(-1, -1, -1)




