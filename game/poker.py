import random
cards = []
while True:
    for i in range(5):
        cards.append(random.randint(1,13))
    if cards.count(cards[0]) != 5:
        break
    cards.clear()
print(' '.join(str(n) for n in cards))

hand = {}
for n in cards:
    if n not in hand.keys():
        hand[n] = cards.count(n)

val = list(hand.values())
if 4 in val:
    print('フォーカード')
elif 2 in val and 3 in val:
    print('フルハウス')
elif 3 in val:
    print('スリーカード')
elif val.count(2) == 2:
    print('ツーペア')
elif val.count(2) == 1:
    print('ワンペア')
else:
    print('ノーハンド')
