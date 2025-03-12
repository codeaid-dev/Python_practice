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
    '''
    temp = ''
    while True:
        a = random.choice(question)
        if a not in temp:
            temp += a
        if len(temp) == 25:
            break'
    question = temp
    '''
    question = ''.join(random.sample(list(question), len(question)))

print(question)
start = time.time()
answer = input('抜けているアルファベットは？')
if answer.upper() == seikai:
    print('正解です')
    end = int(time.time()-start)
    print(f'{end}秒かかりました')
else:
    print(f'間違いです(正解：{seikai})')
