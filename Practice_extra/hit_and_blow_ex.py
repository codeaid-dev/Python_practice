from random import randint
# ランダムに4桁の数値を作成する
digits = []
while len(digits) != 4:
    n = randint(0,9)
    digits.append(n)
target = ''.join(str(n) for n in digits)
print(target)
while True:
    num = ''
    hit, blow = 0, 0
    # 4桁の入力を求める
    while len(num) != 4:
        num = input("数字入力（4桁）：")
    nums = [int(n) for n in list(num)]

    # 入力した4桁とランダムに選んだ4桁を比較する
    # 同じ数値が存在することを考慮してcheckリストに情報を入れる
    check = [None, None, None, None]
    # hitチェック
    for i in range(len(nums)):
        if nums[i] == digits[i]:
            hit += 1
            check[i] = 'hit'
    # blowチェック(ターゲットの数値を基準にチェック)
    for i in range(len(nums)):
        if check[i] == 'hit':
            continue
        for j in range(len(nums)):
            if digits[i] == nums[j]:
                if check[j] != 'hit' and check[j] != 'blow':
                    blow += 1
                    check[j] = 'blow'

    if hit == 4:
        print("クリア！！")
        break
    else:
        print(f"{hit} hit")
        print(f"{blow} blow")
print(f"ターゲット：{target}")
