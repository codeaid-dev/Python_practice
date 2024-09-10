import random
hand = ['グー','チョキ','パー']
win = 0
for i in range(5):
    print(f'{i+1}回目')
    you = int(input('1:グー,2:チョキ,3:パーどれ？>>'))
    com = random.randint(1,3)
    print(f'コンピューターの手：{hand[com-1]}')
    if (you==1 and com==2) or (you==2 and com==3) or (you==3 and com==1):
        print('あなたの勝ち')
        win += 1
    elif (you==1 and com==3) or (you==2 and com==1) or (you==3 and com==2):
        print('コンピューターの勝ち')
    else:
        print('あいこ')
print(f'あなたの勝率は5戦中{win}勝です。')