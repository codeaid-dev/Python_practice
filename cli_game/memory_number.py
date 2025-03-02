import random
import time
import os

level = 1
print("数字記憶ゲームを開始します！")

while True:
    number = "".join(str(random.randint(0, 9)) for _ in range(level))
    print(f"\n{level}桁の数字を覚えてください: {number}")
    time.sleep(3)
    #os.system('cls') # for Windows
    os.system('clear') # for Mac/Linux

    answer = input("覚えた数字を入力してください: ")
    if answer == number:
        print("正解！次のレベルへ進みます。")
        level += 1
    else:
        print(f"間違い！(正解:{number})あなたのレベル: {level}")
        break
