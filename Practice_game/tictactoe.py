import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title('Tic-Tac-Toe')

def click_btn(index):
    pass

btns = []
for i in range(9):
    btns.append(tkinter.Button(root, text='', font=('Helvetica', 20), height=3, width=6, command=lambda: click_btn(i)))

for i in range(9):
    btns[i].grid(row=i//3, column=i%3)

root.mainloop()
