import tkinter
import tkinter.messagebox

btns = []
#True: O, False: X
turn = True
count = 0
def click_btn(button):
    if button.widget['state'] == 'disabled':
        return

    global turn, count
    if button.widget['text'] == '' and turn == True:
        button.widget['text'] = 'O'
        turn = False
        count += 1
        check_win()
    elif button.widget['text'] == '' and turn == False:
        button.widget['text'] = 'X'
        turn = True
        count += 1
        check_win()
    else:
        tkinter.messagebox.showerror('Tic-Tac-Toe', 'すでにクリックされています。\n他のマスを選んでください。')

def disable_btns():
    global btns
    for btn in btns:
        btn['state'] = 'disable'
        #btn.config(state='disable')

winner = 0 # 0:tie, 1:O, 2:X
def check_win():
    global winner
    if btns[0]['text'] == 'O' and btns[1]['text'] == 'O' and btns[2]['text'] == 'O':
        for i in range(3):
            btns[i].config(bg='red')
        winner = 1
    elif btns[3]['text'] == 'O' and btns[4]['text'] == 'O' and btns[5]['text'] == 'O':
        for i in range(3,6):
            btns[i].config(bg='red')
        winner = 1
    elif btns[6]['text'] == 'O' and btns[7]['text'] == 'O' and btns[8]['text'] == 'O':
        for i in range(6,9):
            btns[i].config(bg='red')
        winner = 1
    elif btns[0]['text'] == 'O' and btns[3]['text'] == 'O' and btns[6]['text'] == 'O':
        for i in range(0,7,3):
            btns[i].config(bg='red')
        winner = 1
    elif btns[1]['text'] == 'O' and btns[4]['text'] == 'O' and btns[7]['text'] == 'O':
        for i in range(1,8,3):
            btns[i].config(bg='red')
        winner = 1
    elif btns[2]['text'] == 'O' and btns[5]['text'] == 'O' and btns[8]['text'] == 'O':
        for i in range(2,9,3):
            btns[i].config(bg='red')
        winner = 1
    elif btns[0]['text'] == 'O' and btns[4]['text'] == 'O' and btns[8]['text'] == 'O':
        for i in range(0,9,4):
            btns[i].config(bg='red')
        winner = 1
    elif btns[2]['text'] == 'O' and btns[4]['text'] == 'O' and btns[6]['text'] == 'O':
        for i in range(2,7,2):
            btns[i].config(bg='red')
        winner = 1
    elif btns[0]['text'] == 'X' and btns[1]['text'] == 'X' and btns[2]['text'] == 'X':
        for i in range(3):
            btns[i].config(bg='red')
        winner = 2
    elif btns[3]['text'] == 'X' and btns[4]['text'] == 'X' and btns[5]['text'] == 'X':
        for i in range(3,6):
            btns[i].config(bg='red')
        winner = 2
    elif btns[6]['text'] == 'X' and btns[7]['text'] == 'X' and btns[8]['text'] == 'X':
        for i in range(6,9):
            btns[i].config(bg='red')
        winner = 2
    elif btns[0]['text'] == 'X' and btns[3]['text'] == 'X' and btns[6]['text'] == 'X':
        for i in range(0,7,3):
            btns[i].config(bg='red')
        winner = 2
    elif btns[1]['text'] == 'X' and btns[4]['text'] == 'X' and btns[7]['text'] == 'X':
        for i in range(1,8,3):
            btns[i].config(bg='red')
        winner = 2
    elif btns[2]['text'] == 'X' and btns[5]['text'] == 'X' and btns[8]['text'] == 'X':
        for i in range(2,9,3):
            btns[i].config(bg='red')
        winner = 2
    elif btns[0]['text'] == 'X' and btns[4]['text'] == 'X' and btns[8]['text'] == 'X':
        for i in range(0,9,4):
            btns[i].config(bg='red')
        winner = 2
    elif btns[2]['text'] == 'X' and btns[4]['text'] == 'X' and btns[6]['text'] == 'X':
        for i in range(2,7,2):
            btns[i].config(bg='red')
        winner = 2
    
    if winner == 1:
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'Oの勝ちです。')
        disable_btns()
    elif winner == 2:
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'Xの勝ちです。')
        disable_btns()

    if winner == 0 and count == 9:
        tkinter.messagebox.showinfo('Tic-Tac-Toe', '引き分けです。')
        disable_btns()

root = tkinter.Tk()
root.title('Tic-Tac-Toe')

def reset():
    global btns, turn, count, winner
    btns = []
    turn = True
    count = 0
    winner = 0
    for i in range(9):
        btn = tkinter.Button(root, text='', font=('Helvetica', 20), height=3, width=6)
        btn.grid(row=i//3, column=i%3)
        btn.bind('<ButtonPress>', click_btn)
        btns.append(btn)

my_menu = tkinter.Menu(root)
root.config(menu=my_menu)
options_menu = tkinter.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='オプション', menu=options_menu)
options_menu.add_command(label='リセット', command=reset)
reset()

root.mainloop()
