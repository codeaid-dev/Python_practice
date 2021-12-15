import tkinter
import tkinter.messagebox

btns = []
#True: O, False: X
turn = True
count = 0
def click_btn(button):
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

def check_win():
    global winner
    winner = False
    if btns[0]['text'] == 'X' and btns[1]['text'] == 'X' and btns[2]['text'] == 'X':
        for i in range(3):
            btns[i].config(bg='red')
        winner = True
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'Xの勝ちです。')
    elif btns[3]['text'] == 'X' and btns[4]['text'] == 'X' and btns[5]['text'] == 'X':
        for i in range(3,6):
            btns[i].config(bg='red')
        winner = True
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'Xの勝ちです。')
    elif btns[6]['text'] == 'X' and btns[7]['text'] == 'X' and btns[8]['text'] == 'X':
        for i in range(6,9):
            btns[i].config(bg='red')
        winner = True
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'Xの勝ちです。')
    elif btns[0]['text'] == 'X' and btns[3]['text'] == 'X' and btns[6]['text'] == 'X':
        for i in range(0,7,3):
            btns[i].config(bg='red')
        winner = True
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'Xの勝ちです。')
    elif btns[1]['text'] == 'X' and btns[4]['text'] == 'X' and btns[7]['text'] == 'X':
        for i in range(1,8,3):
            btns[i].config(bg='red')
        winner = True
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'Xの勝ちです。')
    elif btns[2]['text'] == 'X' and btns[5]['text'] == 'X' and btns[8]['text'] == 'X':
        for i in range(2,9,3):
            btns[i].config(bg='red')
        winner = True
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'Xの勝ちです。')
    elif btns[0]['text'] == 'X' and btns[4]['text'] == 'X' and btns[8]['text'] == 'X':
        for i in range(0,9,4):
            btns[i].config(bg='red')
        winner = True
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'Xの勝ちです。')
    elif btns[2]['text'] == 'X' and btns[4]['text'] == 'X' and btns[6]['text'] == 'X':
        for i in range(2,7,2):
            btns[i].config(bg='red')
        winner = True
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'Xの勝ちです。')


root = tkinter.Tk()
root.title('Tic-Tac-Toe')

for i in range(9):
    btn = tkinter.Button(root, text='', font=('Helvetica', 20), height=3, width=6)
    btn.grid(row=i//3, column=i%3)
    btn.bind('<ButtonPress>', click_btn)
    btns.append(btn)

root.mainloop()
