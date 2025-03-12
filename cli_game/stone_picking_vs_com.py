stones = 0
print('石取りゲームを開始します！\nコンピューターと交代で1~3個の石を取ってください。\n最後の1つを取った方が負けとなります。\n必ずコンピューターが勝つようになっています。')

while stones < 10:
    stones = int(input("石の数を入力してください（10個以上)："))

if stones % 4 == 1:
    turn = 2
else:
    turn = 1
while True:
    print(f"石の数：{stones}")
    if stones <= 1:
        break

    if turn == 1:
        print("わたしの番です")
        p1 = 0
        if stones <= 4:
            p1 = stones - 1
        else:
            p1 = (stones - 1) % 4
        print(f"コンピューターは{p1}個取りました")
        turn = 2
        stones -= p1

    else:
        print("あなたの番です")
        p2 = 0
        while p2 < 1 or p2 > 3:
            p2 = int(input("いくつ取りますか？（1〜3個）"))
        turn = 1
        stones -= p2

if stones == 1 and turn == 1:
    print("あなたの勝ちです")
elif stones == 1 and turn == 2:
    print("コンピューターの勝ちです")
elif stones < 1 and turn == 1:
    print("あなたの反則負けです")
elif stones < 1 and turn == 2:
    print("コンピューターの反則負けです")
