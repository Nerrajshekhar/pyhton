# n=input("enter your name")
# a=int(input("enter your age"))
# print("yor name is n and age is a")
# print("your nameis",n,"and your ageis",a)
# print("your name is %s and your age is %d years"%(n,a))
# print("your name is {} and your age is {} years".format(n,a))
# print("your name is {name} and your age is {age} years".format(name=n,age=a))
# print("your name is {name} and your age is {age} years".format(age=a,name=n)) #can change the arguments
# print(f"your name is {n} and your age is {a} years")            #simple way new aded supported only in python 3 onwards




# def checkage(age):
#     if(age.isnumeric()):
#           if(10>int(age)<=110):
#               return 2
#           else:
#               return 1
#     else:
#         return 0
# age=input("enter age")
# flag =checkage(age)
# print(flag)






                       #TOUPLE(3,2,3,42,3)
# x=(2)
# print(type(x))
#
# x=(2,)
# x=[2,3,]
# print(type(x),len(x))

#     DICTINARY
# d1={10:57,20:"vikas",34:40}
# print(d1)
# print(type(d1))
# print(d1[20])
# print(type(d1[20]))
# d1={10:24,20:"vikas",10:40,34:40,10:45,10:36,30:15,10:'raj',60:""}
# print(d1)
# print(type(d1))
# print(d1[10])
# m=d1.values()
# print(m)
# # print(m[0]) #TypeError: 'dict_values' object does not support indexing
# print(type(m))
#
# l1=list(m)  #typecasting
# print(l1)
# for e in m:
#     print(e)
# m=d1.keys()
# print(m)
# m= d1.items()
# print(m)
#
# for e,j in m:   #another form of for loop
#     print(e,j)



# print (7/5)
# print (-7/5)

# d={1:55,3:62,4:99}
# m=d.get(4)
# print(m)
# m=d.pop(3)
# print(m)
# print(d)
# # m=d.pop()  #error
# m=d.popitem()  #to poop last element
# print(m)
# print(d)

# x=d
# y=d.copy()
# x[4]=62
# print(d)
# print(y)
# # d.clear()
# # print(d)
# d.update({3:45,5:62})
# print(d)
# d.setdefault(5,66) #exiting key is not udated
# print(d)
# d.setdefault(9,44)
# print(d)
# l1=[1,2,4]# can also take dictinary at place of list
# d1={}
# # m=d.fromkeys(l1)
# m=d.fromkeys(l1)
# m=d.fromkeys("cetpa")
# print(m)
# m=dict.fromkeys(l1)
# print(m)
     #types of function



# def add(*args):
#     # print(type(args))
#     # print(args)
#     r=0
#     for e in args:
#         r=r+e
#     return r
# m1=add(2,3)
# m2=add(2,3,4,5)
# print(m1,m2)
#
# def add(**kwargs):
#     # print(type(kwargs))
#     # print(kwargs)
#     r=0
#     for e in kwargs.values():
#         r=r+e
#     return r
# m1=add(k1=2,k2=3)
# m2=add(k1=2,k3=3,k2=4,k4=5,abc=5)
# print(m1,m2)

# lambda function

def add(a,b):
    return a+b
m=add(2,3)
print(m)
def checkeven(a):
    return a%2==0
x=43
x=checkeven(x)
print(x)

print(m(x))
x=5
m=lambda a:a%2==0
print(m)


sum= lambda a,b:a+b
print(sum(2,3))  # here sum is not a function it is function pointer