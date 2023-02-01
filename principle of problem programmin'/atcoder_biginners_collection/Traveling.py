# https://atcoder.jp/contests/abs/tasks/arc089_a


N=int(input())
 
t,x,y=0,0,0
 
for _ in range(N):
 
  T,X,Y=map(int, input().split())
 
  l=abs(x-X)+abs(y-Y)
 
  z=T-t-l
 
  if z>=0 and z%2==0:
 
    t,x,y=T,X,Y
 
    continue
 
  else:
 
    print("No")
 
    exit()
 
print("Yes")

