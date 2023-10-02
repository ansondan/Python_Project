
def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('Danny', 'Atlanta', 'Georgia', name="Mike", city="Raleigh", state="North Carolina")