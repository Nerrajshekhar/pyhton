from tkinter import *
import time
import threading
root=Tk()
# def funct1():
#     while(1):
#         # if (count==10000):
#         #     count=0
#         # count+=1
#       for i in range(1000):
#         # root.geometry("300x300+%d+100"%i)
#         root.geometry("%dx%d+%d+%d" % (i,i,i,i))
#         time.sleep(0.001)
i=0
def funct1():
    while(1):
         global  i
         if (i==500):
            i=0
         # for i in range(1000):
         #    # root.geometry("300x300+%d+100"%i)
         root.geometry("%dx%d+%d+%d" % (i,i,i,i))
         i+=1
         root.after(5,funct1)
# root=Tk()
funct1()
# th1=threading.Thread(target=funct1)
# th1.start()
#th1.join()

root.mainloop()
