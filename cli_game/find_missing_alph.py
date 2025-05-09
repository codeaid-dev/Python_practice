import random
import time

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
seikai = random.choice(ALPHABET)
question = ''
for moji in ALPHABET:
    if moji != seikai:
        question += moji

mode = random.randint(1,3)
if mode == 1:
    question = question[::-1]
    #q = sorted(question, reverse=True)
    #question = ''.join(q)
elif mode == 2:
    #question = ''.join(random.sample(list(question), len(question)))
    q = list(question)
    random.shuffle(q)
    question = ''.join(q)

print(question)
start = time.time()
answer = input('抜けているアルファベットは？')
if answer.upper() == seikai:
    print('正解です')
    end = int(time.time()-start)
    print(f'{end}秒かかりました')
else:
    print(f'間違いです(正解：{seikai})')
