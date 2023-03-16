# https://algo-method.com/tasks/1103

N, K = map(int,input().split())
x = list(map(int,input().split()))

# 貪欲法により、電波塔の建てられる本数を返す関数
def build_towers(min_dist):
    ret = 0
    left = -10**9
    for pos in x:
        if (pos - left) >= min_dist:
            ret += 1
            left = pos
    return ret

# 二分探索
left = 1
right = x[N-1]
while (right - left) > 1:
    mid = (left + right) // 2

    # 距離 mid だけ離して K 本以上電波塔を建てることが、
    num_of_towers = build_towers(mid)
    if num_of_towers >= K:
        # 可能ならば可能である側の変数 left を更新、
        left = mid
    else:
        # 不可能ならば不可能である側の変数 right を更新
        right = mid

# 最終的に right - left == 1 となるため、可能なうち最大の距離が left に格納されている
print(left)
