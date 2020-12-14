# from tkinter import *
# def btnHandler(e):
#      btn.place(x=e.x+5,y=e.y+5)
# root=Tk()
# root.geometry("200x200")
# btn=Button(master=root,text="Hello",font=16,bg="yellow")
# root.bind("<Motion>",btnHandler)
# # btn.pack()
#
# root.mainloop()



#NEW PROGRAM MONADY CLASS
#PROGRAM 1
# import tkinter
# root=tkinter.Tk()
# btn1= tkinter.Button(master=root,text="Submit",font=20)
# #root.geometry("400x300")
# root.geometry("400x300+100+150")     #400x300 is dimension of widget and 100 and 150 is the positon of widget on
# # window scale  x axis and y axis respectively
# btn2=tkinter.Button(master=root,text="Hello",font=16,height=3,width=20,bg="orange",fg="red",bd=20)
# btn1.pack()
# btn2.pack()
# # btn1.pack(side='left')   #/right/bottom/top
# # btn1.place(x=5,y=5)
# # btn1.grid(row=0,column=5)  #it also prnt button in widget at row=0 and column=0 as it alwys start from 0,0
# # irespect of row number
# btn1.grid(row=0,column=0)  #cannot use geometry manager grid inside . which already has slaves managed by pack  if use
# # with pack
#
#
#
# root.mainloop()
# # print("hello")

#PROGRAM2  button visit
from tkinter import *
def btnHello_Click():
     print("Hello")
def btnGUI_Click():
     print("GUI")

root=Tk()
root.geometry("400x500+100+200")
btnHello=Button(root,text="hello",font=16,command=btnHello_Click)
btnHello.pack()
btnHello["height"]=7  #other method of declarting the argument
btnHello["bg"]="green"
# btn1.bind("<Click>"hello_Click)
# btn1.grid(row=0,column=0)
btnGUI=Button(root,text="GUI",font=16,command=btnGUI_Click)
btnGUI.pack()



root.mainloop()


#PROGRAM 3 LABEL VISit
from tkinter import *
def btnSubmit_Click():
     name=varentr1.get()
     college=varentr2.get()
     print(name,college)
     varentr1.set("")
     varentr2.set("")

root=Tk()
varentr1=StringVar()
varentr2=StringVar()
root.geometry("400x500+100+200")
label1=Label(master=root,text="my name",font=16)
label1.grid(row=0,column=0)
label2=Label(master=root,text="my college",font=16)
label2.grid(row=1,column=0)
btnSubmit=Button(root,font=16,text="Submit",command=btnSubmit_Click)
btnSubmit.grid(row=2,column=1)
#ENTERY WIDGET
entr1=Entry(root,font=16,textvariable=varentr1)
entr1.grid(row=0,column=1)
entr2=Entry(root,font=16,textvariable=varentr2)
entr2.grid(row=1,column=1)
#event handler for submit button




root.mainloop()



