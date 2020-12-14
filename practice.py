

# N,M=input().split()
# a,b=input().
# c,d=input()
# my_array=numpy.array([a,b],[c,d])
# my_array2=numpy.sum(my_array,axis=0)
# print("The sum along axis0=",numpy.sum(my_array,axis=0))
# print("The product of this sum=",numpy.prod(my_array2))
# nal=[]
# nal1=[]
# list=[]
# for i in range(int(input("do"))):
#         name= input("name")
#         nal.append(name)
#         # print(nal1)
#         # nal[i]=input("name")
#         score = float(input("score"))
#         nal.append(score)
#         # for e in nal1:
#         #      list.append(e)
#         # print(nal1)
#         a=nal.copy()
#         nal1.append(a)
#         print(nal)
#         nal.clear()
# print(nal)
# print(nal1)
# for e in nal1:
#         nal.append(e[1])
# nal.sort(reverse=True)
# print(nal)
# b=[]
#
# for i in range(len(nal)-1):
#         if(nal[i]>nal[i+1]):
#              b.append(nal1[i+1][0])
#         print(b)
# for i in range(len(b)):
#         print(b[0][0])
#         for j in range(len(b[i])):
#           if(ord(b[i][j])>=ord(b[i+1][j])):
#                 b[i],b[i+1]=b[i+1],b[i]
# for i in b:
#         print(i)



# from tkinter import *
# def level_Click():
#     # global level,root1
#     level="easy"
#     # start_game()
#     print(level)
#     root1.destroy()
# def level2_Click():
#     # global level
#     level="hard"
#     print(level)
#     root1.destroy()
#     # start_game()
#
# root1=Tk()
# root1.title("level")
# level1 = Button(master=root1,text="easy",font=16,command=level_Click)
# level1.pack()
# level2 =Button(master=root1,text="hard", font=16,command=level2_Click)
# level2.pack()
# root1.mainloop()

from playsound import playsound
playsound('/path/to/a/sound/file/you/want/to/play.mp3')