S = str(input())

if S[1:7].isdigit()==False:
    print('No')
else:
    mid_int = int(S[1:7])


    if len(S)==8:
        if S[0].isupper()==True & S[7].isupper()==True:
            if 100000 <= mid_int <= 999999:
                print('Yes')
                exit()
            else:
                print('No')
                exit()
        else:
            print('No')
    else:
        print('No')
