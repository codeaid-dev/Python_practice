import random

print('数当てゲームを開始します！1から9の間の数字を3つ当ててください。')
small,large = 1,9
comp = []
while len(comp) < 3:
    n = random.randint(small,large)
    if not n in comp: # 値の重複を防ぐ
        comp.append(n)

attempts = 1
while True:
    while True:
        try:
            nums = list(map(int, input('入力：').split(',')))
            if len(nums) != 3:
                print('数字は3つ入力してください。')
                continue
            for x in nums:
                if not x in range(small,large+1):
                    print('1~9の数字を入力してください。')
                    break
            else:
                break
            '''
            #all関数はiterableの全ての要素がTrueのときTrueを返す(論理積)
            if all(x in range(small,large+1) for x in nums):
                break
            else:
                print('1~9の数字を入力してください。')
            '''
        except ValueError:
            print('1~9の数字を入力してください。')
            continue

    print(f'{attempts}回目：', end='')
    end = 0
    result = []
    for n in range(len(comp)):
        if comp[n] == nums[n]:
            result.append(str(nums[n]))
            end += 1
        else:
            result.append('*')
    print(' '.join(result))
    if end == 3:
        print('当たり！')
        break
    attempts += 1

#print('コンピューター：'+' '.join(str(s) for s in comp))
