def slot():
    import random
    rool = ['●', '■', '▲']
    result = {}
    slot = []
    for i in range(3):
        w = random.randint(0, 2)
        slot.append(rool[w])
    print(' '.join(slot))

    # 絵柄の数を数える
    for i in range(len(rool)):
        result[rool[i]] = slot.count(rool[i])

    score = 0
    for key, val in result.items():
        if val == 3:
            if key == rool[0]:
                score = 100
            elif key == rool[1]:
                score = 200
            else:
                score = 300
    print(score)
    return score

res = 0
for i in range(3):
    print(f'{i+1}回目：')
    input()
    res += slot()
print(f'合計：{res}')
