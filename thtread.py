import threading
def func1():
    for i in range(10):
        print("func1",i)
def func2():
    for i in range(10):
        print("func2",i)
# func1()
# func2()
th1=threading.Thread(target=func1)
th2=threading.Thread(target=func2)
th1.start()
th2.start()
