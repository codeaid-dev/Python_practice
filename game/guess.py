import random

com = random.randint(1,5)

for i in range(3):
    num = int(input('>>'))
    if num == com:
        print(f'あたり！！（コンピューター：{com}）')
        break
else:
    print(f'3回ともあずれでした（コンピューター：{com}）')