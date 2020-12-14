from tkinter import *
import time
root=Tk()
root.title("my window")
#root.geometry("300x300")
while(1):

    for i in range(1000):
            root.geometry("300x300+%d+100"%i)
            #result=self.muovi(root)
            root.after(100)


root.mainloop()


# from tkinter import *
#
# def blink():
#     while(1):
#         e.config(bg='yellow')
#         e.after(1000, lambda: e.config(bg='green')) # after 1000ms
#
# root = Tk()
# e = Entry(root)
# e.pack()
# b = Button(root, text='blink', command=blink)
# b.pack()
# root.mainloop()
