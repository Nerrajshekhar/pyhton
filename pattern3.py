x=[1,2,3,4,5,6,7,8]
x.append(4)
print(x)
x.pop(3) #index location/postion
print(x)
x[0]=5
print(x)
x[0]='hello world'
print(x)
x.pop()
print(x)  # last element will pop by default


x=[[1,2],[4,5],[7,8]]
y=[[1,2],[4,5],[7,8]]
print(id(x),id(y))
print(id(x[0]),id(y[0]))
print(x[0][0],id(x[0][0]),id(y[0][0]))