
def gen_func(n):
    i = 0
    while i < n:
        yield i
        i += 1
result = gen_func(6)
print(type(result))

#for item in result:
    #print(item)

#Lazy evaluation
print(next(result))

print(next(result))

print(next(result))

print(next(result))