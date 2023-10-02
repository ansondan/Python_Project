


while True:
    try:
        x,y = input("Please enter two numbers: ").split(",")
        x,y = int(x),int(y)
        if x == 0:
            x,y=y,x
        z = x/y
        print(x,"/",y,"=",z)
        break
    except ValueError:
        print("That was not a valid number.  Try again...")
    except ZeroDivisionError:
        print("Zero is not valid input. Try again.....")


def pali(x):
    return x == x[::-1]:
print(pali("hello"))
