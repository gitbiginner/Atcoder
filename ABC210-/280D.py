K = int(input())

from math import factorial 


# 答えが x 以下かを判定し、Yes であれば true、No であれば false を返す関数
def check(x, K):
    if factorial(x) % K == 0:
        return True
    return False


# 入力

# 二分探索
# Left は探索範囲の左端を、Right は探索範囲の右端を表す
Left = 2
Right = 10 ** 12
while Left < Right:
	Mid = (Left + Right) // 2
	Answer = check(Mid, K)

	if Answer == False:
		Left = Mid + 1 # 答えが Mid+1 以上であることが分かる
	if Answer == True:
		Right = Mid # 答えが Mid 以下であることが分かる

# 出力（このとき Left=Right になっている）
print(Left)
