# https://atcoder.jp/contests/abc285/tasks/abc285_d
n = int(input())
D = dict(input().split() for i in range(n))
 
while D:
    s, t = D.popitem()
    while t:
        # Pops the key t and returns the value of the key
        # dictionary.pop(key[, default])
        t = D.pop(t, 0)
        if s == t:
            print("No")
            exit(0)
    
print("Yes")
