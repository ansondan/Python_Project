
# def find_sum(*numbers):
#     result = 0
#
#     for num in numbers:
#         result = result + num
#
#     print("Sum = ", result)
#
# list1 = (3, 4, 6, 8)
# find_sum(list1)

def merge_lists(*args):
    return [item for lst in args for item in lst]

print(merge_lists([1, 2], [3, 4], [5, 6]))
