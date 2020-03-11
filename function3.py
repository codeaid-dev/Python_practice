def intro(name, *arguments, **keywords):
    print("あなたは", name, "さんを知っていますか？")
    print(name, "さんは、メジャーで大活躍している選手です。")
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

intro("大谷",
    "彼はピッチャーもバッターもできます。",
    "そして、どちらも成績がとてもいいです！",
    team="エンジェルス",
    position="TWO-WAY（二刀流）",
    years="24歳")