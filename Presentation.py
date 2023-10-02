def add(x, y):
    return x + y
#Decorator function
def square_args(func):
    def inner(x, y):
        return func(x * x, y * y)
    return inner
add = square_args(add)

print(add(2, 3))

@square_args
def add(x, y):
    return x + y

print(add(2, 3))