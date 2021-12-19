import tkinter
import time

root = tkinter.Tk()
root.title('Clock')

time_info = tkinter.Label(root, text='00:00:00', font=('Helvetica',48), fg='green', bg='black')
time_info.pack(pady=20)

root.mainloop()
