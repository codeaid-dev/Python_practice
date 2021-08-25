stones = 0
while stones < 10:
    stones = int(input("石の数を入力してください（10個以上)："))

turn = 1
while True:
    print(f"石の数：{stones}")
    if stones <= 1:
        break

    if turn == 1:
        print("プレイヤー1の番です")
        p1 = 0
        while p1 < 1 or p1 > 3:
            p1 = int(input("いくつ取りますか？（1〜3個）"))
        turn = 2
        stones -= p1

    else:
        print("プレイヤー2の番です")
        p2 = 0
        while p2 < 1 or p2 > 3:
            p2 = int(input("いくつ取りますか？（1〜3個）"))
        turn = 1
        stones -= p2

if stones == 1 and turn == 1:
    print("プレイヤー2の勝ちです")
elif stones == 1 and turn == 2:
    print("プレイヤー1の勝ちです")
elif stones < 1 and turn == 1:
    print("プレイヤー2の反則負けです")
elif stones < 1 and turn == 2:
    print("プレイヤー1の反則負けです")