import tkinter
import random

omikuji = []

def click_btn():
    canvas.delete('omikuji')
    result = random.randint(1,100)
    if 1 <= result <= 2:
        num = 0
    elif 3 <= result <= 12:
        num = 1
    elif 13 <= result <= 32:
        num = 2
    elif 23 <= result <= 62:
        num = 3
    elif 53 <= result <= 82:
        num = 4
    elif 73 <= result <= 92:
        num = 5
    else:
        num = 6

    canvas.create_image(150,330,image=omikuji[num],tags='omikuji')

root = tkinter.Tk()
root.title('おみくじ')
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=300, height=660)
canvas.pack()
box = tkinter.PhotoImage(file='omikuji.png')

for i in range(1,8):
    omikuji.append(tkinter.PhotoImage(file=f'omikuji_fuda{i}.png'))

canvas.create_image(150,330,image=box,tags='omikuji')
button = tkinter.Button(root, text='おみくじを引く', command=click_btn, font=('メイリオ', 36))
button.pack(side=tkinter.BOTTOM, padx=50, pady=50)
root.mainloop()
