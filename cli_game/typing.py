import random
import time

words = ['python', 'programming', 'developer', 'keyboard', 'challenge', 'あいうえお', 'ぱぴぷぺぽ']

print('タイピングゲームを開始！30秒以内にできるだけ多くの単語を入力してください。')
start_time = time.time()
score = 0

while time.time() - start_time < 30:
    word = random.choice(words)
    print(f'単語: {word}')
    user_input = input('入力: ')

    if user_input == word:
        score += 1
        print('正解！')
    else:
        print('間違い！')

print(f'\n終了！スコア: {score}')
