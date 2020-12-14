from tkinter import *
def btnHello_LeftClick(e):
    print(e.x,e.y,e.widget["bg"])
    print("left click")
def btnHello_RightClick(event):
    print("rightclik")
def btnHello_Enter(e):
    btnHello["bg"]="green"
def btnHello_Leave(e):
    btnHello["bg"]="red"
root=Tk()
root.geometry("200x200")
root.config(bg="Orange")
btnHello= Button(root,text="Hello",font=16)
btnHello.place(x=0,y=10)
btnHello.bind("<Button 1>",btnHello_LeftClick)
btnHello.bind("<Button 3>",btnHello_RightClick)
btnHello.bind("<Enter>",btnHello_Enter)
btnHello.bind("<Leave>",btnHello_Leave)

root.mainloop()


# import threading
# import time
# from tkinter import *
# def func1():
#     while(1):
#         count=0
#         if(count==500):
#             count==0
#         count+=5
#     # for i in range(1000):
#         root.geometry("300x300+%d+100"%count)
#         time.sleep(1)
#         root.wait_window(1000)
#
# root=Tk()
# root.geometry("300x200")
# root.title("My CMS")
# #root.maxsize(500,500)
# #root.minsize(100,100)
# #root.state("zoomed")
# th1=threading.Thread(target=func1)
# th1.start()
# th1.join()
#
# root.mainloop()
#
#
#
# # from tkinter import *
# # def btnUp(e):
# #     # btn.place()
# #     global varY,varX
# #     varX+=10
# #     btn.place(x=varX, y=varY)
# #
# # def btnDown(e):
# #     global varX,varY
# #     varX -=10
# #     btn.place(x=varX, y=varY)
# # def btnLeft(e):
# #     global varX, varY
# #     varY += 5
# #     btn.place(x=varX, y=varY)
# # def btnRight(e):
# #     global varX, varY
# #     varY -= 5
# #     btn.place(x=varX, y=varY)
# #     print(e.char,e.keycode,e.keysym)
# # root=Tk()
# # varX,varY=100,100
# # root.geometry("300x200")
# # btn=Button(root,text="Hello")
# # btn.place(x=varX,y=varY)
# # root.bind("<Up>",btnUp)
# # root.bind("<Down>",btnDown)
# # root.bind("a",btnLeft)
# # root.bind("a",btnRight)
# # root.mainloop()
#
# # from  tkinter import *
# # root.Tk()
# #
# # root.m