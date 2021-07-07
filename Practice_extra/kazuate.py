import random
small,large = 1,10
comp = []
for i in range(3):
    comp.append(random.randint(small,large))

for i in range(1,6):
    while True:
        nums = list(map(int, input('入力：').split(',')))
        if len(nums) != 3:
            continue
        for x in nums:
            if not x in range(small,large+1):
                break
        else:
            break
        #if all(x in range(small,large+1) for x in nums): #all関数はiterableの全ての要素がTrueのときTrueを返す(論理積)
            #break

    print(f'{i}回目：')
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

print('コンピューター：'+' '.join(str(s) for s in comp))
