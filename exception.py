# while(1):
#     try:
#         x=input("enter first number")
#         y=input("enter second number")
#         x=int(x)
#         y=int(y)
#         z=x/y
#         print(z)
#     except ValueError:
#         print("Error! Enter inputs in numbers only")
#     except ZeroDivisionError:
#         print("error! enter second inputs non zero")
#     except Exception as err:
#         print("error!",err)

#CALCULUS USING TRY AND EXCEPTION
print("enter numbers to calculate")
while (1):
    try:
        a=int(input("enter first number"))
        b = int(input("enter second number"))
        ch = input("enter choice: +,/,*,-")

        if (ch == '+'):
            a=a+b
            print(a)
        elif (ch == '-'):

            a = a - b
            print(a)
        elif (ch == '*'):

            a=a*b
            print(a)
        elif (ch == '/'):

            a = a / b
            print(a)
        elif (ch == '%'):

            a = a%b
            print(a)
        else:
            raise ValueError("incorrect choice")
            # print ("wrong choice")
    except NotImplementedError as err:
        print("Error!",err)
    # # except ValueError:
    # #     print("Erorr! enter inputs in numbers only")
    # except ZeroDivisionError:
    #     print("Error! enter non zero second input for division")
    # except Exception as er:
    #     print("Error!",er)
