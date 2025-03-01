import random

words = ['python', 'programming', 'computer', 'developer', 'challenge', 'processor']
word = random.choice(words)
guessed_letters = set()
wrong = 6

print('単語当てゲームを開始します！')

while wrong > 0:
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f'\n単語: {display_word}')
    
    if '_' not in display_word:
        print('おめでとう！正解です！')
        break

    guess = input('1文字を入力してください: ').lower()

    if len(guess) != 1 or not guess.isalpha():
        print('無効な入力です。1文字のアルファベットを入力してください。')
        continue

    if guess in guessed_letters:
        print('その文字はすでに使われています。')
        continue

    guessed_letters.add(guess)

    if guess not in word:
        wrong -= 1
        print(f'間違い！残り {wrong} 回のチャンス。')

if '_' in display_word:
    print(f'\nゲームオーバー！正解は {word} でした。')
