from random import randint

uranai = randint(1, 100)
if uranai > 0 and uranai <= 10:
    print('今日は最高！')
elif uranai > 10 and uranai <= 40:
    print('今日はそこそこです')
elif uranai > 40 and uranai <= 80:
    print('今日はまぁまぁ')
else:
    print('今日は最悪です・・')
