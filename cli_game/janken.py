import random

choices = ['グー', 'チョキ', 'パー']
print('じゃんけんを開始します！')

while True:
    print('\n選択肢: 1: グー, 2: チョキ, 3: パー, q: 終了')
    you = input('あなたの手を選んでください（1-3）: ')

    if you == 'q':
        print('ゲームを終了します。')
        break

    if you not in ['1', '2', '3']:
        print('無効な入力です。もう一度入力してください。')
        continue

    you = int(you)-1
    com = random.randint(0, 2)

    print(f'あなた: {choices[you]} vs コンピューター: {choices[com]}')

    if you == com:
        print('引き分けです！')
    elif (you == 0 and com == 1) or \
            (you == 1 and com == 2) or \
            (you == 2 and com == 0):
        print(f'あなたの勝ち！')
    else:
        print(f'コンピューターの勝ち！')
