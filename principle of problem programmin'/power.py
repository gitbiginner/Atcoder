a, b = map(int, input().split())

mod = 10**9+7
#ans = (a**b)%mod
#print(ans) 


def Power(a, b, mod):

    Answer = 1
    for i in range(30):
        wari = 2**i
        if (b//wari) %2 == 1:
            Answer = (Answer*a) % mod

        a = (a*a)% mod
    return Answer

print(Power(a, b, mod))

