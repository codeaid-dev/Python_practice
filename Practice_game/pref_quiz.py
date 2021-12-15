import json
import tkinter
from PIL import Image, ImageTk
import random

with open('prefectures.json', 'r', encoding='utf-8') as f:
    prefs = json.loads(f.read())

correct = None
def questions():
    global correct
    canvas.delete('answer')
    correct = random.randint(0,len(prefs)-1)
    canvas.create_image(250,250,image=prefs[correct]['img'],tags='answer')
    result['text'] = '結果表示'

def click_btn():
    if prefs[correct]['pref'] == answer.get():
        result['text'] = '正解！'
    else:
        result['text'] = f"不正解（正解は{prefs[correct]['pref']}）"
    result.update()

root = tkinter.Tk()
root.title('都道府県クイズ')
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=500, height=500)
canvas.pack()

for d in prefs:
    d['img'] = ImageTk.PhotoImage(Image.open(d['file']))
    #d['img'] = tkinter.PhotoImage(file=d['file'])

tsugi = tkinter.Button(root, text='次の問題', font=('メイリオ', 36), command=questions)
tsugi.pack(side=tkinter.BOTTOM, pady=20)
button = tkinter.Button(root, text='解答', font=('メイリオ', 36), command=click_btn)
button.pack(side=tkinter.BOTTOM, pady=20)
answer = tkinter.Entry(width=20, font=('メイリオ', 20))
answer.pack(side=tkinter.BOTTOM, pady=20)
result = tkinter.Label(root, text='結果表示', font=('メイリオ', 36))
result.pack(side=tkinter.BOTTOM)

questions()
root.mainloop()
