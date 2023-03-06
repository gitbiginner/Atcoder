# https://algo-method.com/tasks/1096

def GCD(A, B):
	if B == 0: return A
	else: return GCD(B, A % B)

n0d0 = input()

n0 = n0d0.split('/')[0]
n0 = int(n0)

d0 = n0d0.split('/')[1]
d0 = int(d0)


g = GCD(n0, d0)
n1 = n0 // g
d1 = d0 // g
#print("%d/%d" % (n1, d1))
print(str(n1)+"/"+str(d1))
        