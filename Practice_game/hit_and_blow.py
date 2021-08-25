from random import randint
# ランダムに4桁の数値を作成する
# 同じ数値が重複しないようにする
digits = []
while len(digits) != 4:
    n = randint(0,9)
    if n not in digits:
        digits.append(n)
target = ''.join(str(n) for n in digits)

while True:
    num = ''
    hit, blow = 0, 0
    # 4桁の入力を求める
    while len(num) != 4:
        num = input("数字入力（4桁）：")
    nums = [int(n) for n in list(num)]

    # 入力した4桁とランダムに選んだ4桁を比較する
    # 同じ数値が重複していないことが前提
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == digits[j]:
                if i == j:
                    hit += 1
                else:
                    blow += 1
                break

    if hit == 4:
        print("クリア！！")
        break
    else:
        print(f"{hit} hit")
        print(f"{blow} blow")
print(f"ターゲット：{target}")
