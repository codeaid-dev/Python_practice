import random

COLORS = ['R', 'G', 'B', 'Y', 'O', 'P']

def create_secret():
    '''ランダムな4つの色の組み合わせを生成'''
    return random.sample(COLORS, 4)

def get_feedback(secret, guess):
    '''正解位置と誤位置の色の数を計算'''
    correct_position = sum(s == g for s, g in zip(secret, guess))
    correct_color = sum(min(secret.count(c), guess.count(c)) for c in COLORS) - correct_position
    return correct_position, correct_color

print('マスターマインドゲームを開始！(R, G, B, Y, O, Pの4色を並べて推理)')
secret = create_secret()

attempts = 0
while True:
    guess = input('4つの色をスペース区切りで入力 (例: R G B Y): ').upper().split()
    if len(guess) != 4 or not all(color in COLORS for color in guess):
        print('無効な入力です。指定された6色の中から4色を入力してください。')
        continue

    attempts += 1
    correct_pos, correct_col = get_feedback(secret, guess)

    print(f'正しい位置の色: {correct_pos}, 含まれるが位置が違う色: {correct_col}')

    if correct_pos == 4:
        print(f'正解！{attempts}回目で当たりました！')
        break
