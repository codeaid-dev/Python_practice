def intro(name, *args, **kwargs):
    print("あなたは", name, "さんを知っていますか？")
    print(name, "さんは、メジャーで大活躍している選手です。")
    for arg in args:
        print(arg)
    print("-" * 40)
    for kw in kwargs:
        print(kw, ":", kwargs[kw])

intro("大谷",
    "彼はピッチャーもバッターもできます。",
    "そして、どちらも成績がとてもいいです！",
    team="エンジェルス",
    position="TWO-WAY（二刀流）",
    years="24歳")