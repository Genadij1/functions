import random
list = []
nums = int(input('length:'))
for i in range(nums):
    list.append(random.randint(0, 100))
def get_unique_number(list):
    unique = []
    for i in list:
        if i not in unique:
            unique.append(i)
    return unique
print(list)
print(get_unique_number(list))
