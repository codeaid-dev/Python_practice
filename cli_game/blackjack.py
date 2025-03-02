import random

def draw_card():
    """カードを1枚引く（A, 2-10, J, Q, K）"""
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return random.choice(cards)

def calculate_score(hand):
    """手札の合計値を計算"""
    values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    score = sum(values[card] for card in hand)
    
    # Aを1にする処理
    ace_count = hand.count('A')
    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1
    
    return score

def blackjack():
    print('ブラックジャックを開始！')

    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    print(f'あなたの手札: {player_hand}, 合計: {calculate_score(player_hand)}')
    print(f'ディーラーの手札: [{dealer_hand[0]}, ?]')

    # プレイヤーのターン
    while calculate_score(player_hand) < 21:
        move = input('ヒット（H）またはスタンド（S）: ').lower()
        if move == 'h':
            player_hand.append(draw_card())
            print(f'あなたの手札: {player_hand}, 合計: {calculate_score(player_hand)}')
        else:
            break

    player_score = calculate_score(player_hand)
    if player_score > 21:
        print('バースト！あなたの負けです。')
        return

    # ディーラーのターン
    print(f'ディーラーの手札: {dealer_hand}, 合計: {calculate_score(dealer_hand)}')
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(draw_card())
        print(f'ディーラーの手札: {dealer_hand}, 合計: {calculate_score(dealer_hand)}')

    dealer_score = calculate_score(dealer_hand)

    # 勝敗判定
    if dealer_score > 21 or player_score > dealer_score:
        print('あなたの勝ち！')
    elif player_score < dealer_score:
        print('ディーラーの勝ち！')
    else:
        print('引き分け！')

if __name__ == '__main__':
    blackjack()