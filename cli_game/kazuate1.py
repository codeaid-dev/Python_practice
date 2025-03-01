import random

print('数当てゲームを開始します！1から100の間の数字を当ててください。')

# 1～100のランダムな数を生成
target_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        #guess = input('あなたの予想: ')
        #if not guess.isdigit():
        #    print('数字を入力してください。')
        #    continue
        #guess = int(guess)
        guess = int(input('あなたの予想: '))
        attempts += 1

        if guess < target_number:
            print('もっと大きい数字です。')
        elif guess > target_number:
            print('もっと小さい数字です。')
        else:
            print(f'おめでとうございます！正解です！{attempts}回目で当たりました。')
            break
    except ValueError:
        print('数字を入力してください。')
