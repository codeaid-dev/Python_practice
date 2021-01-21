from random import randint

cnt = 0
while (True):
    num = randint(1, 20)
    if num % 2 == 0:
        print(num)
        cnt += 1
        if cnt == 10:
            break
'''
for i in range(10):
    num = randint(1, 20)
    if num % 2 == 0:
        print(num)
'''
