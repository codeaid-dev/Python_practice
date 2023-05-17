import tkinter
import random, time

tiles = [i for i in range(1,26)]
random.shuffle(tiles)
nums = []
count = 1
labels = []

root = tkinter.Tk()
root.title('Count Up')
root.geometry('540x540')

def pressed(event):
    global count
    i = event.widget['text']
    if i == count:
        #event.widget.destroy()
        #event.widget.grid_forget()
        event.widget['bg'] = 'white'
        event.widget['text'] = ''
        if count == 25:
            spend = time.time() - start
            for l in labels:
                l.destroy()
            cvs = tkinter.Canvas(root, width=root.winfo_width(), height=root.winfo_height(),bg='white')
            cvs.pack()
            cvs.create_text(root.winfo_width()/2,root.winfo_height()/2,text=f'CLEAR time:{spend:.1f}sec',font=('Helvetica',40),fill='green')
        else:
            count += 1
    else:
        for l in labels:
            l.destroy()
        cvs = tkinter.Canvas(root, width=root.winfo_width(), height=root.winfo_height(),bg='white')
        cvs.pack()
        cvs.create_text(root.winfo_width()/2,root.winfo_height()/2,text='GAME OVER',font=('Helvetica',40),fill='red')

for i in range(25):
    label = tkinter.Label(root, text=tiles[i], font=('Helvetica', 30), width=6, height=3, borderwidth=2, relief='ridge', background='red', foreground='black')
    label.grid(row=i//5, column=i%5)
    label.bind('<ButtonPress>', pressed)
    labels.append(label)

start = time.time()

root.mainloop()