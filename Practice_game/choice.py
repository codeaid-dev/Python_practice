import random
import time

animals = ['ウシ','ウマ','イヌ','サル','ブタ','ネコ','ヘビ']

print('===== スタート =====')
st = time.time()
hit=0
for i in range(5):
    ques = random.randint(0,6)
    random.shuffle(animals)
    disp = ''
    for j in range(7):
        disp += f'{j+1}.{animals[j]} '
    print(disp)
    ans = input(f'{animals[ques]}はどこ？')
    if ans == str(ques+1):
        print('[あたり!]')
        hit+=1
    else:
        print('[はずれ..]')
tt = int(time.time()-st)
print('===== 終了 =====')
print(f'かかった時間は{tt}秒')
print(f'5回中で当てた数は{hit}個')
print(f'スコアは{hit * (100 - tt)}点')