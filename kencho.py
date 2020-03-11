from random import randint

pref = {'北海道':'札幌', '青森県':'青森', '岩手県':'盛岡', '宮城県':'仙台', '栃木県':'宇都宮', '群馬県':'前橋', '神奈川県':'横浜'}
pref_list = ['北海道', '青森県', '岩手県', '宮城県', '栃木県', '群馬県', '神奈川県']

for i in range(5):
    num = randint(0, 6)
    strA = pref_list[num]
    strB = input( strA + "の県庁所在地は？：")
    if (pref[strA] == strB):
        print("正解")
    else:
        print("不正解")
