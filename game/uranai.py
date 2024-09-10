import random

uranai = random.randint(1, 10)
if uranai > 0 and uranai <= 1:
    print('今日は最高！')
elif uranai > 1 and uranai <= 4:
    print('今日はそこそこです')
elif uranai > 4 and uranai <= 8:
    print('今日はまぁまぁ')
else:
    print('今日は最悪・・・')