# https://algo-method.com/tasks/338

# 正規表現を取り扱うためのライブラリ
import re 

# 調べたい文字列を受け取る
S = input() 
# 調べる正規表現 ('r' で囲う)
reg = r'\(.+\)'  

# マッチした文字列情報が格納される (存在しなければnull) 
search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No") 
