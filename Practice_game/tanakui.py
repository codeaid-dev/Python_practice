import tkinter
import random

mouse_x,mouse_y = 0,0
player=None

class Circle:
    def __init__(self,x,y,color,tag):
        self.x=x
        self.y=y
        self.color=color
        self.tag=tag
    def draw(self):
        cvs.delete(self.tag)
        cvs.create_oval(self.x-10,self.y-10,self.x+10,self.y+10,fill=self.color,tags=self.tag)

def motion(e):
    global mouse_x,mouse_y
    mouse_x = e.x
    mouse_y = e.y

def main():
    player.x=mouse_x
    player.y=mouse_y
    player.draw()
    root.after(10, main)

root = tkinter.Tk()
root.title('玉食い')
root.bind('<Motion>', motion)
root.geometry('600x400')
cvs = tkinter.Canvas(root, width=600, height=800, bg='black')
cvs.pack()
player=Circle(300,200,'white','myself')
main()
root.mainloop()