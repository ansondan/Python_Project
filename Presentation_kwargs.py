
def print_all(**kwargs):
    #print out the key-value pairs
    for key, value in kwargs.items():
        print(key + ": " + value)

print_all(name = "Dan", location = "Atlanta", state = "Georgia")