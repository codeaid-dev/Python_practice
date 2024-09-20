import time

st = time.time()
words = ['あいうえお','ぴゃぴゅぴょ','うぉうぃうぇ','ちゃちゅちょ']
for word in words:
    while True:
        s = input(f'「{word}」>>')
        if s == word:
            break
et = int(time.time()-st)
print(f'タイム：{et}秒')