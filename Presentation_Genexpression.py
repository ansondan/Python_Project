
list_result = [2 * num for num in range(10) if num % 2 == 0]

print(list_result)

gen_result = (2 * num for num in range(10) if num % 2 == 0)

print(gen_result)

for item in gen_result:
    print(item)
