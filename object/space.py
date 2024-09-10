import tkinter
import random

class Circle:
    def __init__(self):
        self.x = random.randint(0, 600)
        self.y = random.randint(0, 400)
        self.speed = random.randint(1,6)
        self.color = f'#{int(self.speed/6*255):02x}{int(self.speed/6*255):02x}{int(self.speed/6*255):02x}'
        self.id=None
    def draw(self):
        self.id = cvs.create_oval(self.x-3,self.y-3,self.x+3,self.y+3,fill=self.color,width=0)
    def move(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = 600
        cvs.coords(self.id,self.x-3,self.y-3,self.x+3,self.y+3)

def main():
    for star in stars:
        star.move()
    root.after(10, main)

root = tkinter.Tk()
root.title('宇宙')
root.geometry('600x400')
cvs = tkinter.Canvas(root, width=600, height=400, bg='black')
cvs.pack()
stars = []
for i in range(100):
    c = Circle()
    c.draw()
    stars.append(c)
main()
root.mainloop()